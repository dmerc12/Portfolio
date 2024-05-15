import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Circles from '../../components/Circles';
import { BsArrowRight } from 'react-icons/bs';
import Avatar from '../../components/Avatar';
import { fadeIn } from '../../variants';
import { motion } from 'framer-motion';
import { useState, useEffect } from 'react';

const Contact = () => {
  const [errors, setErrors] = useState({});
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    phone_number: '',
    email: '',
    subject: '',
    message: ''
  });

  useEffect(() => {
    async function fetchCSRFToken() {
      const response = await fetch('http://127.0.0.1:8000/contact/get_csrf_token/');
      const { csrfToken } = await response.json();
    }
    fetchCSRFToken();
  }, []);

  const handleChange = (event) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value
    });
    setErrors({
      ...errors,
      [event.target.name]: ''
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await fetch('http://127.0.0.1:8000/contact/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrfToken},
        body: JSON.stringify(formData)
      });

      if (response.status === 201) {
        toast.success(response.message, {position: 'top-center', autoClose: 3000});
      } else if (response.status === 422) {
        setErrors(response.errors);
      } else if (response.status === 403) {
        toast.warn(response.error, {position: 'top-center', autoClose: 3000});
      } else {
        toast.error('Cannot connect to the back-end, please try again later.', {position: 'top-center', autoClose: 3000});
      }
    } catch (error) {
      toast.error(error.error, {position: 'top-center', autoClose: 3000});
    }
  };

  return (
    <div className='h-full bg-primary/30 my-12 overflow-auto'>
      <div className='container mx-auto py-32 text-center xl:text-left flex items-center justify-center'>
        <div className='flex flex-col w-full max-w-[700px]'>
          <Circles />
          <motion.div variants={fadeIn('right', 0.2)} initial='hidden' animate='show' exit='hidden' className='hidden xl:flex absolute bottom-0 -left-[370px]'>
            <Avatar />
          </motion.div>
          <motion.h2 variants={fadeIn('up', 0.2)} initial='hidden' animate='show' exit='hidden' className='h2 text-center mb-12'>Let's <span className='text-accent'>connect.</span></motion.h2>
          <ToastContainer />
          <motion.form variants={fadeIn('up', 0.4)} initial='hidden' animate='show' exit='hidden' onSubmit={handleSubmit} className='flex-1 flex flex-col gap-6 w-full mx-auto'>
            <div className='flex gap-x-6 w-full'>
              <input type='text' placeholder='first name' className='input' name='first_name' onChange={handleChange} value={formData.first_name} />
              {errors.first_name && (
                <div className='text-red-500'>{errors.first_name}</div>
              )}
              <input type='text' placeholder='last name' className='input' name='last_name' onChange={handleChange} value={formData.last_name} />
              {errors.last_name && (
                <div className='text-red-500'>{errors.last_name}</div>
              )}
            </div>
            <div className='flex gap-x-6 w-full'>
              <input type='text' placeholder='phone number' className='input' name='phone_number' onChange={handleChange} value={formData.phone_number} />
              {errors.phone_number && (
                <div className='text-red-500'>{errors.phone_number}</div>
              )}
              <input type='email' placeholder='email' className='input' name='email' onChange={handleChange} value={formData.email}/>
              {errors.email && (
                <div className='text-red-500'>{errors.email}</div>
              )}
            </div>
            <input type='text' placeholder='subject' className='input' name='subject' onChange={handleChange} value={formData.subject} />
            {errors.subject && (
              <div className='text-red-500'>{errors.subject}</div>
            )}
            <textarea placeholder='message' className='textarea' name='message' onChange={handleChange} value={formData.message}></textarea>
            {errors.first_name && (
              <div className='text-red-500'>{errors.message}</div>
            )}
            <div className='mx-auto'>
              <button className='btn rounded-full border border-white/50 max-w-[170px] px-8 transition-all duration-300 flex items-center justify-center overflow-hidden hover:border-accent group'>
                <span className='group-hover:-translate-y-[120%] groupp-hover:opacity-0 transition-all duration-500'>Let's talk</span>
                <BsArrowRight  className='-translate-y-[120%] opacity-0 group-hover:flex group-hover:-translate-y-0 group-hover:opacity-100 transition-all duration-300 absolute text-[22px]'/>
              </button>
            </div>
            <div className=''></div>
          </motion.form>
        </div>
      </div>
    </div>
  );
};

export default Contact;
