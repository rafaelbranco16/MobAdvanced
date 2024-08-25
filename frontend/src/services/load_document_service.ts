import { url_config } from "../configurations/url_config";
import { endpoints } from "../configurations/endpoints";

export default class DocumentService {
    public async load_document(formData:FormData) {
        try {
            const response = await fetch(url_config.backend_base_url + endpoints.document_loader_endpoint, {
                method: 'POST',
                body: formData,
            });

            const result = await response.json();
            return result.info;
        } catch (error:any) {
            console.error('Error:', error);
            return error.message;
        }
    }

    public async get_all_documents() {
        try {
            const response = await fetch(url_config.backend_base_url + endpoints.get_documents, {
                method: 'GET',
            });
            return await response.json();
        } catch (error:any) {
            console.error('Error:', error);
            return error.message;
        }
    }
    public async downloadDocument(fileName:string) {
        const url = url_config.backend_base_url + endpoints.download_document + fileName

        try {
            const response = await fetch(url, {
                method: 'GET',
            });
            return response;
        } catch (error:any) {
            console.error('Error:', error);
            return error.message;
        }
    }
    public async removeDocument(fileName:string) {
        const url = url_config.backend_base_url + endpoints.remove_document + fileName

        try {
            const response = await fetch(url, {
                method: 'GET',
            });
            return response.json();
        } catch (error:any) {
            console.error('Error:', error);
            return error.message;
        }    
    }

    /**
     * Adds a document to the RAG
     * @param fileName the file name to be added to the RAG on the API
     * @returns if it was added or not
     */
    public async addDocument(fileName:string) {
        const url = url_config.backend_base_url + endpoints.add_document + fileName

        try {
            const response = await fetch(url, {
                method: 'GET',
            });
            return response.json();
        } catch (error:any) {
            console.error('Error:', error);
            return error.message;
        }  
    }
}
