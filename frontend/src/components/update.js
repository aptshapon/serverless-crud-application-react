import React, { useState, useEffect } from 'react';
import { Button, Form } from 'semantic-ui-react'
import axios from 'axios';
import { useHistory, useParams } from 'react-router';

export default function Update() {
    let history = useHistory();
    const { id } = useParams();
    const [book, setBook] = useState({
      bookname: "",
      author: "",
      quantity: "",
      price: ""
    });

    const { bookname, author, quantity, price } = book;
    const onInputChange = e => {
        setBook({ ...book, [e.target.name]: e.target.value });
    };

    useEffect(() => {
      loadUser();
    }, []);

    const onSubmit = async e => {
        e.preventDefault();
        await axios.put(`https://f4tqw8lbre.execute-api.us-east-1.amazonaws.com/book/${id}`, book)
        .then(() => {
            history.push('/read')
        })

    const loadUser = async () => {
        const result = await axios.get(`https://f4tqw8lbre.execute-api.us-east-1.amazonaws.com/book/${id}`);
        setBook(result.data);
        };
    return (
        <div>
            <Form key={book.id} className="create-form">
                <Form.Field>
                    <label>Book Name</label>
                    <input placeholder='Book Name' value={bookname} onChange={(e) => onInputChange(e)}/>
                </Form.Field>
                <Form.Field>
                    <label>Author</label>
                    <input placeholder='Author' value={author} onChange={(e) => onInputChange(e)}/>
                </Form.Field>
                <Form.Field>
                    <label>Quantity</label>
                    <input placeholder='Quantity' value={quantity} onChange={(e) => onInputChange(e)}/>
                </Form.Field>
                <Form.Field>
                    <label>Price</label>
                    <input placeholder='Price' value={price} onChange={(e) => onInputChange(e)}/>
                </Form.Field>
                <Button type='submit' onClick={e => onSubmit(e)}>Update</Button>
            </Form>
        </div>
    )
}}