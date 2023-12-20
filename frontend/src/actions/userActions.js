import { CONNECT_REQUEST, CONNECT_FAIL, CONNECT_SUCCESS, USER_LOGIN_FAIL, USER_LOGIN_REQUEST, USER_LOGIN_SUCCESS, USER_LOGOUT, USER_REGISTER_FAIL, USER_REGISTER_REQUEST, USER_REGISTER_SUCCESS } from "../constants/userConstants"
import axios from 'axios'

const URL = 'http://localhost:8000/run_be'

export const login = (username, password) => async (dispatch) => {
    try {
        dispatch({
            type:USER_LOGIN_REQUEST
        })
        
        const formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);

        const config = {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        };

        const { data } = await axios.post(
            `${URL}/auth/login`,
            formData,
            config
        );


        dispatch({
            type: USER_LOGIN_SUCCESS,
            payload: data
        })

        localStorage.setItem('userInfo', JSON.stringify(data))
    } catch (error) {
        dispatch({
            type: USER_LOGIN_FAIL,
            payload: 
                error.response && error.response.data.message
                ? error.response.data.message
                : error.message
        })
    }
}

export const logout = () => (dispatch) => {
    localStorage.removeItem('userInfo')
    dispatch({type: USER_LOGOUT})
}

export const register = (username, password, student_id, full_name, gender, org_name, org_name_child, year_study) => async (dispatch) => {
    try {
        dispatch({
            type: USER_REGISTER_REQUEST
        })

        const config = {
            headers: {
                'Content-Type': 'application/json'
            }
        }

        const {data} = await axios.post(`${URL}/user/register`, {username, password, student_id, full_name, gender, org_name, org_name_child, year_study}, config)

        dispatch({
            type: USER_REGISTER_SUCCESS,
            payload: data
        })

        dispatch({
            type: USER_LOGIN_SUCCESS,
            payload: data
        })

        localStorage.setItem('userInfo', JSON.stringify(data))
    }
    catch (error) {
        dispatch({
            type: USER_REGISTER_FAIL,
            payload: 
            error.response && error.response.data.message 
            ? error.response.data.message
            : error.message
        })
    }
} 

export const connect = (code) => async (dispatch, getState) => {
    try {
        dispatch({
            type: CONNECT_REQUEST
        })

        const { userLogin: {userInfo}} = getState()
        
        const config = {
            headers: {
                Authorization: `Bearer ${userInfo.accessToken}`,
                Accept: "application/json"
            },
        }

        const {data} = await axios.post(`${URL}/user/authorize-code?authorizecode=${code}`, null, config)
        dispatch({
            type: CONNECT_SUCCESS,
            payload: data
        })

    }
    catch (error) {
        dispatch({
            type: CONNECT_FAIL,
            payload: 
            error.response && error.response.data.message 
            ? error.response.data.message
            : error.message
        })
    }
} 