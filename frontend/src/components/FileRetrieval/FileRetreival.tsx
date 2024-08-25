import { useState, useEffect } from 'react';
import DocumentService from '../../services/load_document_service';
import './FileRetreival.css';
import ConfirmationDialog from '../ConfirmDialog/ConfirmDialog';

// Define the structure of the file object
interface File {
    file_name: string;
    type: string;
    download_url: string; // Add this to match the structure of the backend response
}

function FileRetreival() {
    const [items, setItems] = useState<File[]>([]);
    const [isDialogOpen, setIsDialogOpen] = useState<boolean>(false);
    const [itemToRemove, setItemToRemove] = useState<string | null>(null);
    const service:DocumentService = new DocumentService()
    type ActionCallback = (item: string) => Promise<any>;
    const handleRemove = (item: string) => {
        setItemToRemove(item);
        setIsDialogOpen(true);
      };
    
      const handleConfirm = async (actionCallback:ActionCallback) => {
        if (itemToRemove) {
          const response = await actionCallback(itemToRemove)
          console.log(response)
        }
        setItemToRemove(null);
        setIsDialogOpen(false);
        const response = await service.get_all_documents();
        setItems(response.documents);
      };
    
      const handleCancel = () => {
        setItemToRemove(null);
        setIsDialogOpen(false);
      };

    const handleDownload = async (fileName: string) => {
        try {
            //Fetch the file content
            const response = await new DocumentService().downloadDocument(fileName);
          
            if (!response.ok) {
                console.error('Failed to fetch file:', response.statusText);
            return;
            }

            //Start the download
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = fileName;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            window.URL.revokeObjectURL(url);
        } catch (error) {
            console.error('Error during file download:', error);
        }
    };

    useEffect(() => {
        const fetchItems = async () => {
            try {
                const doc_service = new DocumentService();
                const response = await doc_service.get_all_documents();
                
                setItems(response.documents);
            } catch (error) {
                console.error('Error fetching documents:', error); 
            }
        };

        fetchItems();
    }, []);

    return (
        <div className="file-retrieval">
            <ul>
                {items.map((item, index) => (
                    <li key={index} className="file-retrieval-item">
                        <div className="file-retrieval-file">
                            {item.file_name} ({item.type})
                        </div>
                        <div className="file-retrieval-actions">
                            <button
                                className="file-retrieval-actions-download"
                                onClick={() => handleDownload(item.file_name)}
                            >
                                Download
                            </button>
                            <button 
                                className="file-retrieval-actions-remove"
                                onClick={() => handleRemove(item.file_name)}    
                            >Remove</button>
                            <ConfirmationDialog
                                isOpen={isDialogOpen}
                                onConfirm={() => handleConfirm(service.removeDocument)}
                                onCancel={handleCancel}
                                message={`Are you sure you want to remove ${itemToRemove}?`}
                            />

                            <button 
                                className="file-retrieval-actions-add"
                                onClick={() => handleRemove(item.file_name)}    
                            >Add</button>
                            <ConfirmationDialog
                                isOpen={isDialogOpen}
                                onConfirm={() => handleConfirm(service.addDocument)}
                                onCancel={handleCancel}
                                message={`Are you sure you want to add ${itemToRemove}?`}
                            />
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default FileRetreival;
