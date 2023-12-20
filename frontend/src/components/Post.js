import React from 'react'
import { Card } from 'react-bootstrap'
import { Link } from 'react-router-dom'

const Post = ({post}) => {
  return (
    <Card className='my-3 py-3 rounded'>
      <Link to={`/post/${post._id}`}>
        <Card.Img src={post.image} variant='top' />
      </Link>

      <Card.Body>
        <Link to={`/post/${post._id}`}>
            <Card.Title as='div'>
                <strong>{post.name}</strong>
            </Card.Title>
        </Link>
      </Card.Body>
    </Card>
  )
}

export default Post
