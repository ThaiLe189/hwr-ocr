import axios from 'axios'
import queryString from 'query-string'
import { Status } from '../constants/Constants'
import { _IApiResponse } from '../interfaces/IApiResponse'
import { _IBodyError } from '../interfaces/IBodyError'



let bodyError: _IBodyError;


const dataError = (errorCode: any, message: any) => {
    try {
        bodyError = {
            errorCode: errorCode,
            message: message
        }
    } catch (e) {
        bodyError = {
            errorCode: Status.UNKNOW_ERROR,
            message: 'Unknow error, please try again later'
        }
    }

}

const statusCode = (status: any, message: any) => {
    if (status == Status.INTERNAL_SERVER_ERROR) {
        console.log('Có lỗi hệ thống, vui lòng thử lại', "error");
    } else if (status === Status.NOTFOUND) {
        console.log('Lỗi hệ thống không kết nối được đến server', "error");
    } else if (status == Status.FORBIDDEN) {
        console.log('Lỗi FORBIDDEN', "error");
        // localStorage.removeItem('token')
        // localStorage.removeItem('storagePassword')
        // window.location.href = '/login'
    } else if (status == Status.UNAUTHORIZED) {
        console.log('Lỗi authen', "error");
        localStorage.removeItem("token")
        // localStorage.setItem('logout-event', 'logout' + Math.random());
        // window.open(`${window.location.origin}/auth/login`, "_self")
        // window.location.href = '/login'
    } else if (status == Status.BAD_REQUEST) {
        console.log('Lỗi BAD REQUEST', "error");
        // Toast(message, "error");
    }
}

const axiosClient = axios.create({
    baseURL: process.env.REACT_APP_URL_BE || "http://localhost:5000",
    paramsSerializer: (params) => queryString.stringify(params)
})

axiosClient.interceptors.request.use(async (config) => {
    // Handle token here ...
    return config
})

axiosClient.interceptors.response.use(
    (response) => {
        const apiResponse: _IApiResponse = {
            status: response.status,
            body: response.data
        }
        return apiResponse
    },
    (error) => {
        dataError(error.response.data.errorCode, error.response.data.message)
        statusCode(error.response.status, error.response.data.message)

        const apiResponse: _IApiResponse = {
            status: error.response.status,
            body: bodyError
        }
        return apiResponse
    }
)


export default axiosClient;

// window.addEventListener('storage', onStorageUpdate)

export async function getRequest(path: any): Promise<_IApiResponse> {
    return await axios.get(process.env.REACT_APP_URL_BE || "http://localhost:5000" + path)
        .then(
            (response) => {
                const apiResponse: _IApiResponse = {
                    status: response.status,
                    body: response.data,
                };
                return apiResponse;
            },
            (error) => {
                dataError(error.response.data.errorCode, error.response.data.message)
                statusCode(error.response.status, error.response.data.message)

                const apiResponse: _IApiResponse = {
                    status: error.response.status,
                    body: bodyError
                }
                return apiResponse
            }
        );

}

export function axiosRequest(method: any, path: any, params: object, isUpload?: boolean): Promise<_IApiResponse> {

    return new Promise<_IApiResponse>((resolve) => {
        axios({
            data: JSON.stringify(params),
            method: method,
            url: process.env.REACT_APP_URL_BE || "http://localhost:5000" + path
        })
            .then(function (response) {
                resolve({
                    status: response.status,
                    body: response.data
                });
            })
            .catch(function (error) {
                dataError(error.response.data.errorCode, error.response.data.message)
                statusCode(error.response.status, error.response.data.message)

                const apiResponse: _IApiResponse = {
                    status: error.response.status,
                    body: bodyError
                }
                return apiResponse
            });

    });
}

export async function postRequest(path: any, params: object, isUpload?: boolean): Promise<_IApiResponse> {
    return axiosRequest("POST", path, params, isUpload)
}

export async function putRequest(path: any, params: object): Promise<_IApiResponse> {
    return axiosRequest("PUT", path, params)
}

export async function deleteRequest(path: any, params: object): Promise<_IApiResponse> {
    return axiosRequest("DELETE", path, params)
}
