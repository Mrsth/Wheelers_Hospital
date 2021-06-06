import React, { useState, useEffect} from 'react';
import {Form, Input, Button} from 'antd';
import { ToastContainer, toast } from 'react-toastify';
import {Redirect} from 'react-router-dom';

// import AntRegister from './AntRegister';
import AntNav from './AntNav';
import AntRegister from './AntRegister';

import axios from 'axios';

const AntOTP = (props) =>{

    // const [allData, setAllData] = useState([])
    const [phn, setPhn] = useState("")
    const [votp, setVOTP] = useState("")
    const x = 1;
    const[form] = Form.useForm();

    const handleSubmit = (values) => {
        console.log('Success:', values);
        axios.get(`http://127.0.0.1:8000/api/otp/${phn}/${x}`)
        .then(res=>{
            console.log("ok = ",res)
            if(res.data !== "OTP Not Sent"){
                toast.success(`OTP sent to phone ${phn}`)
            }else{
                toast.error(`Failed to sent OTP to phone ${phn}`)
            }
        })
        // form.resetFields();
    };

    const handleOTPVerification = (values) => {
        console.log('Success:', values);
        console.log('PROPS = ', props);
        axios.post(`http://127.0.0.1:8000/api/otp/${phn}/${votp}`)
        .then(res=>{
            console.log("ok = ",res)
            if(res.data == 'OTP Verified'){
                props.history.push('/reg')
            }else{
                toast.error(`Failed to verify OTP`)
            }
        });        
    };

    const onFinishFailed = (errorInfo) => {
        console.log('Failed:', errorInfo);
    };
    return(
        <div>
            <AntNav/>
            <ToastContainer/>
            <Form
                name="basic"
                initialValues={{
                    remember: true,
                }}
                form={form}
                onFinish={handleSubmit}
                onFinishFailed={onFinishFailed}
                style={{maxWidth:'20%', marginTop:'10%', marginLeft:'40%'}}
                >
                <h2>Enter your phone number to get the OTP</h2>
                <Form.Item
                    label = "Phone number"
                    name="phn"
                    rules={[
                    {
                        required: true,
                        message: 'Please input your phone number!',
                    },
                    ]}
                >
                    <Input onChange={e=>setPhn(e.target.value)}/>
                </Form.Item>
                <Form.Item>
                    <Button style={{color:"white", background:'black'}} htmlType="submit">
                    Get OTP
                    </Button>
                </Form.Item>
            </Form>    
            <Form
                style={{maxWidth:'20%', marginTop:'3%', marginLeft:'40%'}}
                onFinish={handleOTPVerification}
            >
                <Form.Item
                        label = "Enter the OTP"
                        name="votp"
                        rules={[
                        {
                            required: true,
                            message: 'Please input your otp number!',
                        },
                        ]}
                    >
                    <Input onChange={e=>setVOTP(e.target.value)}/>
                </Form.Item>
                <Form.Item>
                    <Button style={{color:"white", background:'black'}} htmlType="submit">
                        Verify my OTP
                    </Button>
                </Form.Item>
                <a href="http://localhost:3000/">Go back to landing page</a> 
            </Form>           
        </div>
    );
}

export default AntOTP;