import ParticclesContainer from '../components/ParticlesContainer';
import ProjectsBtn from '../components/ProjectsBtn';
import Avatar from '../components/Avatar';
import { motion } from 'framer-motion';
import { fadeIn } from '../variants';
import Image from 'next/image';

const Home = () => {
  return (
    <div className='bg-primary/60 h-full'>
      <div className='w-full h-full bg-gradient-to-r from-primary/10 via-black/30 to-black/10'>
        <div className='text-center flex flex-col justify-center xl:pt-40 xl:text-left h-full container mx-auto'>
          <motion.h1 variants={fadeIn('down', 0.2)} initial='hidden' animate='show' exit='hidden' className='h1'>Hello There! <br/> I'm <span className='text-accent'>Dylan Mercer</span></motion.h1>
          <motion.p variants={fadeIn('down', 0.3)} initial='hidden' animate='show' exit='hidden' className='max-w-sm xl:max-w-lx mx-auto xl:mx-0 mb-10 xl:mb-16'>I'm a full stack software developer comfortable in a multitude of hats. Check out my projects or contact me to see if I may be a good fit for your project!</motion.p>
          <div className='flex justify-center xl:hidden relative'>
            <ProjectsBtn />
          </div>
          <motion.div variants={fadeIn('down', 0.4)} initial='hidden' animate='show' exit='hidden' className='hidden xl:flex'>
            <ProjectsBtn />
          </motion.div>
        </div>
      </div>
      <div>image</div>
    </div>
  );
};

export default Home;
