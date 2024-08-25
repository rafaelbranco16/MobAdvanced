import { url_config } from "../configurations/url_config";
import { endpoints } from "../configurations/endpoints";


export async function send_question(question:string, class_name:string) {
    const url = 
        url_config.backend_base_url + 
        endpoints.send_question + 
        '?question=' + question + '&' + 'class_name=' + class_name

    try {
        const response = await fetch(url, {
            method: 'GET',
        });
        return await response.json();
    } catch (error:any) {
        return error.message;
    }  
}