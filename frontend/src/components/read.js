import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { Table, Button } from 'semantic-ui-react';
import { Link } from 'react-router-dom';

export default function Read() {
    const [APIData, setAPIData] = useState([]);
    useEffect(() => {
        axios.get(`https://w46c72arhg.execute-api.us-east-1.amazonaws.com/books`)
            .then((response) => {
                console.log(response.data)
                setAPIData(response.data);
            })
    }, []);

    const setData = (data) => {
        let { id, bookname, author, quantity, price } = data;
        localStorage.setItem('ID', id);
        localStorage.setItem('Book Name', bookname);
        localStorage.setItem('Book Author', author);
        localStorage.setItem('Quantity', quantity);
        localStorage.setItem('Book Price', price);
    }

    const getData = () => {
        axios.get(`https://w46c72arhg.execute-api.us-east-1.amazonaws.com/books`)
            .then((getData) => {
                setAPIData(getData.data);
            })
    }

    const onDelete = (id) => {
        axios.delete(`https://57gsm3qtde.execute-api.us-east-1.amazonaws.com/book/${id}`)
        .then(() => {
            getData();
        })
    }

    return (
        <div>
            <Table singleLine>
                <Table.Header>
                    <Table.Row>
                        <Table.HeaderCell>Book Name</Table.HeaderCell>
                        <Table.HeaderCell>Book Author</Table.HeaderCell>
                        <Table.HeaderCell>Quantity</Table.HeaderCell>
                        <Table.HeaderCell>Book Price</Table.HeaderCell>
                        <Table.HeaderCell>Update</Table.HeaderCell>
                        <Table.HeaderCell>Delete</Table.HeaderCell>
                    </Table.Row>
                </Table.Header>

                <Table.Body>
                    {APIData.map((data) => {
                        return (
                            <Table.Row>
                                <Table.Cell>{data.bookname}</Table.Cell>
                                <Table.Cell>{data.author}</Table.Cell>
                                <Table.Cell>{data.quantity}</Table.Cell>
                                <Table.Cell>{data.price}</Table.Cell>
                                <Link to='/update'>
                                    <Table.Cell> 
                                        <Button onClick={() => setData(data)}>Update</Button>
                                    </Table.Cell>
                                </Link>
                                <Table.Cell>
                                    <Button onClick={() => onDelete(data.id)}>Delete</Button>
                                </Table.Cell>
                            </Table.Row>
                        )
                    })}
                </Table.Body>
            </Table>
        </div>
    )
}
