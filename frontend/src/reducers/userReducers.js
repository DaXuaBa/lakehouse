import { 
    CONNECT_FAIL,
    CONNECT_REQUEST,
    CONNECT_SUCCESS,
    USER_LOGIN_FAIL, 
    USER_LOGIN_REQUEST, 
    USER_LOGIN_SUCCESS, 
    USER_LOGOUT,
    USER_REGISTER_FAIL,
    USER_REGISTER_REQUEST
} from "../constants/userConstants";


export const userLoginReducer = (state = { }, action) => {
    switch (action.type) {
        case USER_LOGIN_REQUEST:
            return { loading: true}
        case USER_LOGIN_SUCCESS:
            return { loading: false, userInfo: action.payload }
        case USER_LOGIN_FAIL:
            return { loading: false, error: action.payload }
        case USER_LOGOUT:
            return {}
        default:
            return state
    }
}

export const userRegisterReducer = (state = {}, action) => {
    switch (action.type) {
        case USER_REGISTER_REQUEST:
            return { loading: true}
        case USER_LOGIN_SUCCESS:
            return { loading: false, userInfo: action.payload }
        case USER_REGISTER_FAIL:
            return { loading: false, error: action.payload }
        default:
            return state
    }
}

export const connectReducer = (state = {user: {}}, action) => {
    switch (action.type) {
        case CONNECT_REQUEST:
            return { loading: true}
        case CONNECT_SUCCESS:
            return { loading: false, acp: action.payload }
        case CONNECT_FAIL:
            return { loading: false, error: action.payload }
        default:
            return state
    }
}