import { url_config } from "../configurations/url_config";
import { endpoints } from "../configurations/endpoints";

export default class LoadDocumentService {
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
}
