import React from 'react'
import { Link, useParams } from 'react-router-dom'
import { Row, Col, Image, ListGroup, Card } from 'react-bootstrap'
import posts from '../posts'

const PostSrceen = () => {
    const {id} = useParams()

    const post = posts.find(p => p._id === id)

  return ( 
    <>
        <Link className='btn btn-dark my-3' to='/'>Trở về</Link>
        <Row>
            <Col md={5}>
                <div style={{ border: '2px solid #ccc', borderRadius: '8px', overflow: 'hidden' }}>
                    <Image src={post.image} alt={post.name} fluid/>
                </div>
            </Col>
            <Col md={4}>
                <ListGroup variant='flush'>
                    <ListGroup.Item>
                        <h3>{post.name}</h3>
                    </ListGroup.Item>
                    <ListGroup.Item style={{ textAlign: 'justify' }}>
                        {post.description}
                    </ListGroup.Item>
                </ListGroup>
            </Col>
            <Col md={3}>
                <Card>
                    <ListGroup variant='flush'>
                        <ListGroup.Item>
                            <Row>
                                <Col>
                                    Ngày viết:
                                </Col>
                                <Col>
                                    <strong>{post.created_at}</strong>
                                </Col>
                            </Row>
                        </ListGroup.Item>

                        <ListGroup.Item>
                            <Row>
                                <Col>
                                    Người viết:
                                </Col>
                                <Col>
                                    <strong>{post.created_user}</strong>
                                </Col>
                            </Row>
                        </ListGroup.Item>
                    </ListGroup>
                </Card>
            </Col>
        </Row>
    </>
  )
}

export default PostSrceen
