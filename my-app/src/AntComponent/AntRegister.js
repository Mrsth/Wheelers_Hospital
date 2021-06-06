import React, {useState} from 'react';
import { Form, Input, Button, Alert} from 'antd';
import axios from 'axios';
import {UserOutlined, LockOutlined, MailFilled} from '@ant-design/icons';
import AntNav from "./AntNav";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import AntOTP from './AntOTP';


const AntRegister = props =>{


        const[username, setUserName] = useState("");
        const[email, setEmail] = useState("");
        const[password, setPassWord] = useState("");
        const[phone, setPhone] = useState("");

    
        const [showSuccessAlert, setSuccessAlert] = useState();
        const [error, setError] = useState("")

        const[form] = Form.useForm();

        const layout = {
            labelCol: { span: 8 },
            wrapperCol: { span: 16 },
        };

      
        const handleSubmit = (values) => {
          console.log('Success:', values);
          console.log(username, password);
    
              axios.post('http://127.0.0.1:8000/api/register', 
              {
                  'username': username,
                  'email':email,
                  'password': password,
                  'phone_number': phone
              }).then(res=>{
                  console.log(res.data.token)
                    toast.success("User Created successfully")
                    form.resetFields();
                    <AntOTP/>
                }
                ).catch(()=>{
                    setError(true)
                    toast.error("Registrations Failed")
                    form.resetFields();
                })
               
        };

      
      
        const onFinishFailed = (errorInfo) => {
          console.log('Failed:', errorInfo);
        };


    return(
        <div>
            <AntNav/>
            <ToastContainer/>
            <div style={{width:'30%', marginTop:'10%', marginLeft:'41%'}}>
            {/* {
                showSuccessAlert && 
                
                <Alert message="Signup Completed" type="success" 
                description="User account has been created" 
                showIcon 
                style={{maxWidth:"30em", fontWeight:"bold"}}/>
                
            }

            {
                    error && 
                    <center>
                    <Alert message="Signup Failed" type="error" 
                    description = "Please input valid inputs"
                    showIcon 
                    style={{maxWidth:"30em", fontWeight:"bold"}}/>
                    </center>
            } */}
            <h1>Sign Up</h1>
            <Form
                form={form}
                {...layout}
                name="basic"
                initialValues={{
                    remember: true,
                }}
                onFinish={handleSubmit}
                onFinishFailed={onFinishFailed}
                >
                <Form.Item
                    name="username"
                    rules={[
                    {
                        required: true,
                        message: 'Please input your username!',
                    },
                    ]}
                >
                    <Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="Username" onChange={e=>setUserName(e.target.value)} id="demo1"/>
                </Form.Item>

                <Form.Item
                    name="email"
                    rules={[
                    {
                        required: true,
                        message: 'Please input your email!',
                    },
                    ]}
                >
                    <Input  placeholder="Email" prefix={<MailFilled className="site-form-item-icon"/>} onChange={e=>setEmail(e.target.value)} id="demo2"/>
                </Form.Item>

                <Form.Item
                    name="phone"
                    rules={[
                    {
                        required: false,
                        message: 'Please input your phone number!',
                    },
                    ]}
                >
                    <Input  placeholder="Phone number" prefix={<MailFilled className="site-form-item-icon"/>} onChange={e=>setPhone(e.target.value)} id="demo4"/>
                </Form.Item>

                <Form.Item
                    name="password"
                    rules={[
                    {
                        required: true,
                        message: 'Please input your password!',
                    },
                    ]}
                >
                    <Input.Password  placeholder="Password" prefix={<LockOutlined className="site-form-item-icon" />} onChange={e=>setPassWord(e.target.value)} id="demo3"/>
                </Form.Item>

                <Form.Item>
                    <Button style={{color:"white", background:'black'}} htmlType="submit">
                    Sign Up
                    </Button>
                </Form.Item>
                </Form>
        </div>
        {/* <Link style={{marginLeft:'41%'}} to='/'>Already have an account? Go back to Login Page</Link> */}
        </div>
    );
}

export default AntRegister;