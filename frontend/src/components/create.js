import React, { useState } from 'react';
import { Button, Form } from 'semantic-ui-react'
import axios from 'axios';
import { useHistory } from 'react-router';


export default function Create() {
    let history = useHistory();
    const [bookname, setBookName] = useState('');
    const [author, setAuthor] = useState('');
    const [quantity, setQuantity] = useState('');
    const [price, setPrice] = useState('');
    const postData = () => {
        axios.post(`https://gamqgunwfg.execute-api.us-east-1.amazonaws.com/books`, {
            bookname,
            author,
            quantity,
            price,
        }).then(() => {
            history.push('/read')
        })
    }
    return (
        <div>
            <Form className="create-form">
                <Form.Field>
                    <label>Book Name</label>
                    <input placeholder='Enter name of book' onChange={(e) => setBookName(e.target.value)}/>
                </Form.Field>
                <Form.Field>
                    <label>Book Author</label>
                    <input placeholder='Enter name of author' onChange={(e) => setAuthor(e.target.value)}/>
                </Form.Field>
                <Form.Field>
                    <label>Quantity</label>
                    <input placeholder='Enter available quantity' onChange={(e) => setQuantity(e.target.value)}/>
                </Form.Field>
                <Form.Field>
                    <label>Book Price</label>
                    <input placeholder='Enter price of book' onChange={(e) => setPrice(e.target.value)}/>
                </Form.Field>
                <Button color="blue" onClick={postData} type='submit'>Submit</Button>
            </Form>
        </div>
    )
}
