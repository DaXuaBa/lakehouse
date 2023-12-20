import React from 'react'
import { useDispatch, useSelector} from 'react-redux'
import { LinkContainer } from 'react-router-bootstrap'
import { Navbar, Nav, Container, NavDropdown } from 'react-bootstrap'
import { logout } from '../actions/userActions'

const Header = () => {
  const dispatch = useDispatch()
  const userLogin = useSelector(state => state.userLogin)
  const { userInfo } = userLogin

  const logoutHandler = () => {
    dispatch(logout())
  }

  return (<header>
    <Navbar bg="dark" variant="dark" expand="lg" collapseOnSelect>
      <Container>
        <LinkContainer to='/'>
            <Navbar.Brand>LakeHouse</Navbar.Brand>
        </LinkContainer>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ms-auto">
            {userInfo ? (
              <NavDropdown title={userInfo ? userInfo['Họ và Tên'] : 'Tài khoản'}>
                <LinkContainer to='/connectstrava'>
                  <NavDropdown.Item>Kết nối với Strava</NavDropdown.Item>
                </LinkContainer>
                <NavDropdown.Item onClick={logoutHandler}>Đăng Xuất</NavDropdown.Item>
              </NavDropdown>
            ) : 
            <LinkContainer to='/login'>
            <Nav.Link>
              <i className='fas fa-user'></i> Đăng Nhập
            </Nav.Link>
          </LinkContainer>}
            
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  </header>
)}

export default Header