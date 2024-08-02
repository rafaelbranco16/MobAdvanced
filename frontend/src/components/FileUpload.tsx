// src/components/FileUpload.tsx

import React, { useState, ChangeEvent } from 'react';
import DocumentService from '../services/load_document_service';

const FileUpload: React.FC = () => {
    const [file, setFile] = useState<File | null>(null);
    const [message, setMessage] = useState<string>('');

    const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
        if (event.target.files) {
            setFile(event.target.files[0]);
        }
    };

    const handleUpload = async () => {
        if (!file) {
            setMessage('Please select a file first!');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        const service:DocumentService = new DocumentService()    
        setMessage(await service.load_document(formData))    
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload</button>
            {message && <p>{message}</p>}
        </div>
    );
};

export default FileUpload;
