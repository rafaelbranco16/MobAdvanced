import { url_config } from "../configurations/url_config";
import { endpoints } from "../configurations/endpoints";


async function send_question(question:string) {
    const url = url_config.backend_base_url + endpoints.send_question

    try {
        const response = await fetch(url, {
            method: 'GET',
        });
        return response.json();
    } catch (error:any) {
        return error.message;
    }  
}