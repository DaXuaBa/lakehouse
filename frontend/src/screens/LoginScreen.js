import React, {useState, useEffect} from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { Form, Button, Row, Col} from 'react-bootstrap'
import {useDispatch, useSelector} from 'react-redux'
import Message from '../components/Message'
import Loader from '../components/Loader'
import FormContainer from '../components/FormContainer'
import {login} from '../actions/userActions'

const LoginScreen = ({location}) => {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const dispatch = useDispatch()
    const navigate = useNavigate();

    const userLogin = useSelector(state => state.userLogin)
    const { loading, error, userInfo} = userLogin

    const redirect = location?.search ? location.search.split('=')[1] : '/';

    useEffect(() => {
        if(userInfo) {
            navigate(redirect)
        }
    }, [ userInfo, redirect, navigate])

    const submidHandler = (e) => {
        e.preventDefault()
        dispatch(login(username,password))
    }

  return (
  <FormContainer>
    <h1>Đăng Nhập</h1>
    {error && <Message variant='danger'>{error}</Message>}
    {loading && <Loader />}
    <Form onSubmit={submidHandler}>
        <Form.Group controlId='username'>
            <Form.Label>Tên Tài Khoản</Form.Label>
            <Form.Control 
                tpye='username' 
                placeholder='Nhập tài khoản' 
                value={username} 
                onChange={(e) => setUsername(e.target.value)}>
            </Form.Control>
        </Form.Group>

        <Form.Group controlId='password'>
            <Form.Label>Mật Khẩu</Form.Label>
            <Form.Control 
                type='password' 
                placeholder='Nhập mật khẩu' 
                value={password} 
                onChange={(e) => setPassword(e.target.value)}>
            </Form.Control>
        </Form.Group>

        <Button type='submit' variant='primary'>
            Đăng Nhập
        </Button>
    </Form>

    <Row className='py-3'>
        <Col>
            Bạn chưa có tài khoản?{' '}
            <Link to={redirect ? `/register?redirect=${redirect}` : '/register'}>
                Đăng ký tại đây
            </Link>
        </Col>
    </Row>
  </FormContainer>
  )
}

export default LoginScreen
