import React, {useState, useEffect} from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { Form, Button, Row, Col} from 'react-bootstrap'
import {useDispatch, useSelector} from 'react-redux'
import Message from '../components/Message'
import Loader from '../components/Loader'
import FormContainer from '../components/FormContainer'
import {register} from '../actions/userActions'
import yearStudyOptions from '../options/yearstudy'
import orgNameOptions from '../options/orgname'
import orgNameChildOptions from '../options/orgnamechild'

const RegisterScreen = ({location}) => {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [confirmPassword, setConfirmPassword] = useState('')
    const [student_id, setId] = useState('')
    const [full_name, setFullname] = useState('')
    const [gender, setGender] = useState('')
    const [org_name, setOrg] = useState('')
    const [org_name_child, setOrgchild] = useState('')
    const [year_study, setYearstudy] = useState('')
    const [phone, setPhone] = useState('')
    
    const dispatch = useDispatch()
    const navigate = useNavigate();

    const userRegister = useSelector(state => state.userRegister)
    const { loading, error, userInfo} = userRegister

    const redirect = location?.search ? location.search.split('=')[1] : '/';

    useEffect(() => {
        if(userInfo) {
            navigate(redirect)
        }
    }, [ userInfo, redirect, navigate])

    const submidHandler = (e) => {
        e.preventDefault()
        dispatch(register(username, password, student_id, full_name, gender, org_name, org_name_child, year_study))

    }

    return (
        <FormContainer>
            <h1>Đăng Ký tài khoản</h1>
            {error && <Message variant='danger'>{error}</Message>}
            {loading && <Loader />}
            <Form onSubmit={submidHandler}>
            <Row>
                <Col xs={6}>
                <Form.Group controlId='username'>
                    <Form.Label>Tài khoản *</Form.Label>
                    <Form.Control 
                        tpye='username' 
                        placeholder='Nhập tài khoản' 
                        value={username} 
                        onChange={(e) => setUsername(e.target.value)}>
                    </Form.Control>
                </Form.Group>
                </Col>

                <Col xs={6}>
                <Form.Group controlId='full_name'>
                    <Form.Label>Họ và Tên *</Form.Label>
                    <Form.Control 
                        type='full_name' 
                        placeholder='Nhập họ và tên' 
                        value={full_name} 
                        onChange={(e) => setFullname(e.target.value)}>
                    </Form.Control>
                </Form.Group>
                </Col>              
                </Row>

                <Row>
                <Col xs={6}>
                <Form.Group controlId='password'>
                    <Form.Label>Mật khẩu *</Form.Label>
                    <Form.Control 
                        type='password' 
                        placeholder='' 
                        value={password} 
                        onChange={(e) => setPassword(e.target.value)}>
                    </Form.Control>
                </Form.Group>
                </Col>

                <Col xs={6}>
                <Form.Group controlId='confirmPassword'>
                    <Form.Label>Xác nhận mật khẩu *</Form.Label>
                    <Form.Control 
                        type='password' 
                        placeholder='' 
                        value={confirmPassword} 
                        onChange={(e) => setConfirmPassword(e.target.value)}>
                    </Form.Control>
                </Form.Group>
                </Col>
                </Row>

                <Row>
                <Col xs={6}>
                <Form.Group controlId='student_id'>
                    <Form.Label>Mã số sinh viên *</Form.Label>
                    <Form.Control 
                        type='student_id' 
                        placeholder='Nhập mã số sinh viên' 
                        value={student_id} 
                        onChange={(e) => setId(e.target.value)}>
                    </Form.Control>
                </Form.Group>
                </Col>

                <Col xs={6}>
                <Form.Group controlId='gender'>
                    <Form.Label>Giới tính *</Form.Label>
                    <Form.Control as="select" value={gender} onChange={(e) => setGender(e.target.value)}>
                        <option value="">Chọn giới tính</option>
                        <option value="Nam">Nam</option>
                        <option value="Nu">Nữ</option>
                        <option value="Other">Khác</option>
                    </Form.Control>
                </Form.Group>
                </Col>
                </Row>

                <Row>
                <Col xs={6}>
                <Form.Group controlId='org_name'>
                    <Form.Label>Khoa *</Form.Label>
                    <Form.Control 
                        as="select"
                        value={org_name} 
                        onChange={(e) => setOrg(e.target.value)}>
                        {orgNameOptions.map((option) => (
                        <option key={option.value} value={option.value}>
                            {option.label}
                        </option>
                        ))}
                    </Form.Control>
                </Form.Group>
                </Col>

                <Col xs={6}>
                <Form.Group controlId='org_name_child'>
                    <Form.Label>Ngành *</Form.Label>
                    <Form.Control 
                        as="select"
                        value={org_name_child} 
                        onChange={(e) => setOrgchild(e.target.value)}>
                        {orgNameChildOptions.map((option) => (
                        <option key={option.value} value={option.value}>
                            {option.label}
                        </option>
                        ))}
                    </Form.Control>
                </Form.Group>
                </Col>
                </Row>

                <Row>
                <Col xs={6}>
                <Form.Group controlId='year_study'>
                    <Form.Label>Khóa học *</Form.Label>
                    <Form.Control 
                        as="select"
                        value={year_study} 
                        onChange={(e) => setYearstudy(e.target.value)}>
                        {yearStudyOptions.map((option) => (
                        <option key={option.value} value={option.value}>
                            {option.label}
                        </option>
                        ))}
                    </Form.Control>
                </Form.Group>
                </Col>

                <Col xs={6}>
                <Form.Group controlId='phone'>
                    <Form.Label>Số điện thoại</Form.Label>
                    <Form.Control 
                        type='phone' 
                        placeholder='Nhập số điện thoại' 
                        value={phone} 
                        onChange={(e) => setPhone(e.target.value)}>
                    </Form.Control>
                </Form.Group>
                </Col>
                </Row>

                <Row className='py-3 text-center'>
                <Col>
                    <Button type='submit' variant='primary'>
                        Đăng Ký
                    </Button>
                </Col>
                </Row>
            </Form>

            <Row className='py-3'>
                <Col>
                    Đã có tài khoản rồi?{' '}
                    <Link to={redirect ? `/login?redirect=${redirect}` : '/login'}>
                        Đăng Nhập
                    </Link>
                </Col>
            </Row>
        </FormContainer>
    )
}

export default RegisterScreen