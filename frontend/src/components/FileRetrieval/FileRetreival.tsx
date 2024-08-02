import React, { useState, useEffect } from 'react';
import DocumentService from '../../services/load_document_service';
import File from './File'; // Import your File interface

function FileRetreival() {
    const [items, setItems] = useState<File[]>([]); // Specify type for items array

    useEffect(() => {
        const fetchItems = async () => {
            try {
                const doc_service = new DocumentService();
                const response = await doc_service.get_all_documents();
                
                console.log(response.documents); // Log the fetched documents
                setItems(response.documents); // Set items with the fetched documents
            } catch (error) {
                console.error('Error fetching documents:', error); 
            }
        };

        fetchItems(); 
    }, []); 

    return (
        <>
            <div className="file-retreival">
                <ul>
                    {items.map((item, index) => (
                        <li key={index}>
                            {item.file_name} ({item.type}) {/* Render file_name and type */}
                        </li>
                    ))}
                </ul>
            </div>
        </>
    );
}

export default FileRetreival;
