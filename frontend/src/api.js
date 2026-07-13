import axios from "axios";

const API = axios.create({
    baseURL: "https://multimodal-ophthalmology-ai.onrender.com",
    timeout: 120000
});

export const predictDisease = async (file) => {

    const formData = new FormData();

    formData.append("file", file);

    const response = await API.post(
        "/predict",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data"
            }
        }
    );

    return response.data;
};


export const generateGradCAM = async (file) => {

    const formData = new FormData();

    formData.append("file", file);

    const response = await API.post(
        "/gradcam",
        formData,
        {
            responseType: "blob"
        }
    );

    return URL.createObjectURL(response.data);

};


export const askChatbot = async (question) => {

    const response = await API.post(
        "/chat",
        {
            question
        }
    );

    return response.data;

};


export const downloadReport = async (file) => {

    const formData = new FormData();

    formData.append("file", file);

    const response = await API.post(
        "/report",
        formData,
        {
            responseType: "blob"
        }
    );

    return URL.createObjectURL(response.data);

};


export default API;