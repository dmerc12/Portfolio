import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Circles from '../../components/Circles';
import { BsArrowRight } from 'react-icons/bs';
import Avatar from '../../components/Avatar';
import { fadeIn } from '../../variants';
import { motion } from 'framer-motion';
import { useState } from 'react';

const Contact = () => {
  const [formattedPhoneNumber, setFormattedPhoneNumber] = useState('');
  const [errors, setErrors] = useState({});
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    phone_number: '',
    email: '',
    subject: '',
    message: ''
  });

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

  const handlePhoneChange = (e) => {
    const rawValue = e.target.value;
    const digits = rawValue.replace(/\D/g, '');
    let formatted = digits;
    if (digits.length > 3 && digits.length <= 6) {
      formatted = `${digits.slice(0,3)}-${digits.slice(3)}`;
    } else if (digits.length > 6) {
      formatted = `${digits.slice(0,3)}-${digits.slice(3,6)}-${digits.slice(6,10)}`;
    }
    setFormattedPhoneNumber(formatted);
    setFormData({ ...formData, phone_number: formatted });
  }

  const handleSubmit = async (event) => {
    event.preventDefault();
    const endpointUrl = 'https://formspree.io/f/mjgzjlzd';
    try {
      const completeFormData = {
        ...formData,
        phone_number: formattedPhoneNumber
      };

      const response = await fetch(endpointUrl, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(completeFormData)
      });

      if (response.ok) {
        setFormData({first_name: '', last_name: '', phone_number: '', email: '', subject: '', message: ''})
        setFormattedPhoneNumber('')
        toast.success('Message sent successfully! I will be in contact soon.', {position: 'top-center', autoClose: 3000});
      } else {
        toast.error('Oops! There was a problem submitting your form.', {position: 'top-center', autoClose: 3000});
      }
    } catch (error) {
      toast.error('Network error. Please check your connection and try again.', {position: 'top-center', autoClose: 3000});
    }
  };

  return (
    <div className='h-full bg-primary/30 my-12 overflow-auto'>
      <div className='container mx-auto py-32 text-center xl:text-left flex items-center justify-center'>
        <div className='flex flex-col w-full max-w-[700px]'>
          <Circles />
          <motion.div variants={fadeIn('right', 0.2)} initial='hidden' animate='show' exit='hidden' className='hidden xl:flex absolute bottom-0 -left-[370px] z-0 opacity-70'>
            <Avatar />
          </motion.div>
          <motion.h2 variants={fadeIn('up', 0.2)} initial='hidden' animate='show' exit='hidden' className='h2 text-center mb-12'>Let's <span className='text-accent'>connect.</span></motion.h2>
          <ToastContainer />
          <motion.form variants={fadeIn('up', 0.4)} initial='hidden' animate='show' exit='hidden' onSubmit={handleSubmit} className='flex-1 flex flex-col gap-6 w-full mx-auto z-10'>
            <div className='flex gap-x-6 w-full'>
              <div className='flex flex-col w-1/2'>
                <input required type='text' placeholder='first name' className='input' name='first_name' onChange={handleChange} value={formData.first_name} />
                {errors.first_name && (
                  <div className='text-red-500 text-center pt-4'>{errors.first_name}</div>
                )}
              </div>
              <div className='flex flex-col w-1/2'>
                <input required type='text' placeholder='last name' className='input' name='last_name' onChange={handleChange} value={formData.last_name} />
                {errors.last_name && (
                  <div className='text-red-500 text-center pt-4'>{errors.last_name}</div>
                )}
              </div>
            </div>
            <div className='flex gap-x-6 w-full'>
              <div className='flex flex-col w-1/2'>
                <input required type='text' placeholder='phone number' className='input' name='phone_number' onChange={handlePhoneChange} value={formattedPhoneNumber} />
                {errors.phone_number && (
                  <div className='text-red-500 text-center pt-4'>{errors.phone_number}</div>
                )}
              </div>
              <div className='flex flex-col w-1/2'>
                <input required type='email' placeholder='email' className='input' name='email' onChange={handleChange} value={formData.email}/>
                {errors.email && (
                  <div className='text-red-500 text-center pt-4'>{errors.email}</div>
                )}
              </div>
            </div>
            <div className='flex flex-col'>
              <input required type='text' placeholder='subject' className='input' name='subject' onChange={handleChange} value={formData.subject} />
              {errors.subject && (
                <div className='text-red-500 text-center pt-4'>{errors.subject}</div>
              )}
            </div>
            <div className='flex flex-col'>
              <textarea required placeholder='message' className='textarea' name='message' onChange={handleChange} value={formData.message}></textarea>
              {errors.message && (
                <div className='text-red-500 text-center pt-4'>{errors.message}</div>
              )}
            </div>
            <div className='mx-auto'>
              <button className='btn rounded-full border border-white/50 max-w-[170px] px-8 transition-all duration-300 flex items-center justify-center overflow-hidden hover:border-accent group'>
                <span className='group-hover:-translate-y-[120%] group-hover:opacity-0 transition-all duration-500'>Let's talk</span>
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
