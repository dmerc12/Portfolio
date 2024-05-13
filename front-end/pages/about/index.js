import { SiNextdotjs, SiDjango, SiMysql, SiPostgresql, SiSqlite, SiSelenium, SiPytest, SiJunit5, SiTailwindcss } from 'react-icons/si';
import { FaHtml5, FaCss3, FaJs, FaReact, FaPython, FaJava, FaGitAlt, FaBootstrap, FaAws, FaFlask } from 'react-icons/fa';
import Circles from '../../components/Circles';
import Avatar from '../../components/Avatar';
import { fadeIn } from '../../variants';
import { motion } from 'framer-motion';
import CountUp from 'react-countup';
import { useState } from 'react';

const aboutData = [
  {
    title: 'skills',
    info: [
      {
        title: 'Front-End Development',
        icons: [<FaHtml5 />, <FaCss3 />, <FaJs />, <FaReact />, <SiNextdotjs />, <FaBootstrap />, <SiTailwindcss />],
      },
      {
        title: 'Back-End Development',
        icons: [<FaPython />, <FaJava />, <SiDjango />, <FaFlask />],
      },
      {
        title: 'Database Development',
        icons: [<SiMysql />, <SiPostgresql />, <SiSqlite />],
      },
      {
        title: 'Cloud Computing',
        icons: [<FaAws />],
      },
      {
        title: 'Testing',
        icons: [<SiSelenium />, <SiPytest />, <SiJunit5 />],
      },
      {
        title: 'Version Control',
        icons: [<FaGitAlt />],
      },
    ],
  },
  {
    title: 'experience',
    info: [
      {
        title: 'Help Desk Analyst - Apex Systems',
        stage: '2023 - present',
      },
      {
        title: 'QA Full Stack Developer - Revature',
        stage: '2022 - 2023',
      },
      {
        title: 'Assembly Technician - National Assemblers Inc.',
        stage: '2021 - 2022',
      },
      {
        title: 'Assistant Ops Manager - Little Guys Movers',
        stage: '2017 - 2020',
      },
    ],
  },
  {
    title: 'credentials',
    info: [
      {
        title: 'Certified Cloud Practitioner - AWS',
        stage: '2024',
      },
      {
        title: 'ITF+ - CompTIA',
        stage: '2022',
      },
      {
        title: 'Associate Degree - Oklahoma City Community College',
        stage: '2020',
      },
      {
        title: 'Honors Diploma - Blanchard High School',
        stage: '2016',
      },
    ],
  },
];

const About = () => {
  const [index, setIndex] = useState(0);

  return (
    <div className='h-full bg-primary/30 py-32 text-center xl:text-left'>
      <Circles />
      <motion.div variants={fadeIn('right', 0.2)} initial='hidden' animate='show' exit='hidden' className='hidden xl:flex absolute bottom-0 -left-[370px]'>
        <Avatar />
      </motion.div>
      <motion.div>
        <div className='container mx-auto h-full flex flex-col items-center xl:flex-row gap-x-6 mt-[60px]'>
          <div className='flex-1 flex flex-col justify-center'>
            <motion.h2 variants={fadeIn('right', 0.2)} initial='hidden' animate='show' exit='hidden' className='h2'>Captivating <span className='text-accent'>stories</span> birth magnificient designs.</motion.h2>
            <motion.p variants={fadeIn('right', 0.4)} initial='hidden' animate='show' exit='hidden' className='max-w-[500px] mx-auto xl:mx-0 mb-6 xl:mb-12 px-2 xl:px-0'>Four years ago, I began putting to use a coding class I took early in my academic career with more in-depth project-based learning. Since then, I've learned a lot and even built my own PC. I've worked as a full-stack developer where I not only became more familiar with every step of the SDLC but also the work that goes into each step. I've learned that to be good at software development, you must be able to learn new things at a moment's notice.</motion.p>
            <motion.p variants={fadeIn('right', 0.6)} initial='hidden' animate='show' exit='hidden' className='max-w-[500px] mx-auto xl:mx-0 mb-6 xl:mb-12 px-2 xl:px-0'>After being a part of a mass layoff in 2023, I decided to sharpen my skills with more personal projects and started on a degree in Computer Science and Software Development with an expected graduation date in 2026. Some projects I've either collaborated on or completed myself include, but aren't limited to: social media applications, finance applications, e-commerce and inventory management applications, and even my own JARVIS application.</motion.p>
            <motion.div variants={fadeIn('right', 0.8)} initial='hidden' animate='show' exit='hidden' className='hidden md:flex md:max-w-xl xl:max-w-none mx-auto xl:mx-0 mb-8'>
              <div className='flex flex-1 xl:gap-x-6'>
                <div className='relative flex-1 after:w-[1px] after:h-full after:bg-white/10 after:absolute after:top-0 after:right-0'>
                  <div className='text-2xl xl:text-4xl front-extrabold text-accent mb-2'>
                    <CountUp start={0} end={4} duration={5} /> +
                  </div>
                  <div className='text-xs uppercase tracking-[1px] leading-[1.4] max-w-[100px]'>Years of experience</div>
                </div>
                <div className='relative flex-1 after:w-[1px] after:h-full after:bg-white/10 after:absolute after:top-0 after:right-0'>
                  <div className='text-2xl xl:text-4xl front-extrabold text-accent mb-2'>
                    <CountUp start={0} end={5} duration={5} /> +
                  </div>
                  <div className='text-xs uppercase tracking-[1px] leading-[1.4] max-w-[100px]'>Satisfied clients</div>
                </div>
                <div className='relative flex-1'>
                  <div className='text-2xl xl:text-4xl front-extrabold text-accent mb-2'>
                    <CountUp start={0} end={10} duration={5} /> +
                  </div>
                  <div className='text-xs uppercase tracking-[1px] leading-[1.4] max-w-[100px]'>Finished projects</div>
                </div>
              </div>
            </motion.div>
          </div>
          <motion.div variants={fadeIn('left', 0.4)} initial='hidden' animate='show' exit='hidden' className='flex flex-col w-full xl:max-w-[48%] h-[480px]'>
              <div className='flex gap-x-4 xl:gap-x-8 mx-auto xl:mx-0 mb-4'>
                {aboutData.map((item, itemIndex) => {
                  return <div key={itemIndex} className={`${index === itemIndex && 'text-accent after:w-[100%] after:bg-accent after:transition-all after:duration-300'} cursor-pointer capitalize xl:text-lg relative after:w-8 after:h-[2px] after:bg-white after:absolute after:-bottom-1 after:left-0`} onClick={() => setIndex(itemIndex)}>{item.title}</div>
                })}
              </div>
              <div className='py-2 xl:py-6 flex flex-col gap-y-2 xl:gap-y-4 items-center xl:items-start'>
                {aboutData[index].info.map((item, itemIndex) => {
                  return (
                    <div key={itemIndex} className='flex-1 flex flex-col md:flex-row max-w-max gap-x-2 items-center text-white/60'>
                      <div className='font-light mb-2 md:mb-0'>{item.title}</div>
                      <div className='hidden md:flex'>-</div>
                      <div>{item.stage}</div>
                      <div className='flex gap-x-4'>
                        {item.icons?.map((icon, itemIndex) => {
                          return <div className='text-2xl text-white'>{icon}</div>
                        })}
                      </div>
                    </div>
                  )
                })}
              </div>
          </motion.div>

        </div>
      </motion.div>
    </div>
  );
};

export default About;
