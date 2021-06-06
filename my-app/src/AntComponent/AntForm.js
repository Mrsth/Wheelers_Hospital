import React, {useEffect, useState} from 'react';
import { Form, Input, Button} from 'antd';
import axios from 'axios';
import {useHistory} from 'react-router-dom';
import {UserOutlined, LockOutlined} from '@ant-design/icons';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const AntForm = props =>{

        let history = useHistory();

        const[username, setUserName] = useState("");
        const[password, setPassWord] = useState("");


        const [form] = Form.useForm();

        const layout = {

            labelCol: { span: 8 },
            wrapperCol: { span: 16 },
        };

       
      
        const onFinish = (values) => {
              axios.post('http://127.0.0.1:8000/api/login', 
              {
                  'username': username,
                  'password': password
              }).then(res=>{
                  console.log("RES = ",res.data)
                  localStorage.setItem('token', res.data.token)
                  localStorage.setItem('user',username)
                  localStorage.setItem('uid',res.data.uid)
                  history.push('/dash')
                }).catch(err=>{
                    toast.error("Login Failed")
                    form.resetFields();
                })
        };
      
        const onFinishFailed = (errorInfo) => {
          console.log('Failed:', errorInfo);
        };

        useEffect(()=>{
            if(localStorage.getItem('token') !==  null){
                history.push('/dash')
            }
        },[localStorage.getItem('token')])
         
    return(
        <div style={{marginTop:'20%'}}>
            <ToastContainer/>
            <h1>Login</h1>
                <Form
                    {...layout}
                    form={form}
                    name="basic"
                    initialValues={{
                        remember: true,
                    }}
                    onFinish={onFinish}
                    onFinishFailed={onFinishFailed}
                    style={{}}
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
                        <Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="Username" onChange={e=>setUserName(e.target.value)}/>
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
                        <Input.Password  placeholder="Password" prefix={<LockOutlined className="site-form-item-icon" />} onChange={e=>setPassWord(e.target.value)}/>
                    </Form.Item>

                    <Form.Item>
                        <Button style={{background:'black', color:'white'}} htmlType="submit">
                        Login
                        </Button>
                    </Form.Item>
                    </Form>
        </div>
    );
}

export default AntForm;