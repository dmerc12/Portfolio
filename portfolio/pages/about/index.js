import { SiNextdotjs, SiDjango, SiMysql, SiPostgresql, SiSqlite, SiSelenium, SiPytest, SiJunit5, SiTailwindcss, SiSpring, SiGithubactions, SiRailway, SiCloudflare, SiTypescript, SiExpress } from 'react-icons/si';
import { FaHtml5, FaCss3, FaJs, FaReact, FaPython, FaJava, FaGitAlt, FaBootstrap, FaAws, FaFlask, FaAngular, FaDocker, FaAndroid } from 'react-icons/fa';
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
        icons: [<FaHtml5 />, <FaCss3 />, <FaJs />, <SiTypescript/>, <FaReact />, <FaAngular />, <SiNextdotjs />, <FaBootstrap />, <SiTailwindcss />],
      },
      {
        title: 'Back-End Development',
        icons: [<FaPython />, <FaJava />, <SiTypescript />, <SiSpring />, <SiDjango />, <FaFlask />, <SiExpress />],
      },
      {
        title: 'Containerization & CI/CD Tools',
        icons: [<FaGitAlt />, <FaDocker />, <SiGithubactions />, <FaAws />],
      },
      {
        title: 'Database Development',
        icons: [<SiMysql />, <SiPostgresql />, <SiSqlite />],
      },
      {
        title: 'Cloud Deployment',
        icons: [<FaAws />, <SiRailway />, <SiCloudflare />],
      },
      {
        title: 'Mobile Development',
        icons: [<FaAndroid/>]
      },
      {
        title: 'Testing',
        icons: [<SiSelenium />, <SiPytest />, <SiJunit5 />],
      },
    ],
  },
  {
    title: 'experience',
    info: [
      {
        title: 'Substitute Teacher - Buchanan Elementary School',
        stage: '2024 - present'
      },
      {
        title: 'Help Desk Analyst - Apex Systems',
        stage: '2023 - 2024',
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
        title: 'Certified Back-End Developer - WGU',
        stage: '2026'
      },
      {
        title: 'Certified Front-End Developer - WGU',
        stage: '2025'
      },
      {
        title: 'Foundation in IT Service Management - ITIL 4',
        stage: '2025'
      },
      {
        title: 'Project+ - CompTIA',
        stage: '2024',
      },
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

  // Calculate the years of experience dynamically
  const startYear = 2021;
  const currentYear = new Date().getFullYear();
  const yearsOfExperience = currentYear - startYear;
  const finishedProjects = 10;

  return (
    <div className='h-full bg-primary/30 py-32 text-center xl:text-left overflow-auto'>
      <Circles />
      <motion.div variants={fadeIn('right', 0.2)} initial='hidden' animate='show' exit='hidden' className='hidden xl:flex absolute bottom-0 -left-[720px] z-0 opacity-70'>
        <Avatar />
      </motion.div>
      <motion.div className=' relative z-10'>
        <div className='container mx-auto h-full flex flex-col items-center xl:flex-row gap-x-6 mt-[60px]'>
          <div className='flex-1 flex flex-col justify-center'>
            <motion.h2 variants={fadeIn('right', 0.2)} initial='hidden' animate='show' exit='hidden' className='h2'>
              From full-stack to <span className='text-accent'>fourth grade</span>. And back again.
            </motion.h2>
            <motion.p variants={fadeIn('right', 0.4)} initial='hidden' animate='show' exit='hidden' className='max-w-[500px] mx-auto xl:mx-0 mb-6 xl:mb-12 px-2 xl:px-0'>
              Four years ago, I finally put that intro coding class to work building real things.
              Since then, I've gone from hobbyist to full-stack developer, survived a mass layoff,
              cut my teeth on an enterprise helpdesk, and built my own PC from scratch.
              I've learned that great software isn't just about syntax;
              it's about adapting on the fly, whether that's debugging a production bug at 2 AM or explaining fractions to a room full of fourth graders.
            </motion.p>
            <motion.p variants={fadeIn('right', 0.6)} initial='hidden' animate='show' exit='hidden' className='max-w-[500px] mx-auto xl:mx-0 mb-6 xl:mb-12 px-2 xl:px-0'>
              The layoff in 2023 was a reset. I enrolled at WGU for my Software Engineering degree (expected June 2026)
              and started treating every course project like a client deliverable.
              Meanwhile, I've spent two years substitute teaching across all grade levels, from kindergarten to 4th grade,
              often switching rooms mid-day.
              Nothing teaches you clarity, patience, and on-your-feet problem-solving like a class of 30 kids with an unresponsive touchscreen.
            </motion.p>
            <motion.div variants={fadeIn('right', 0.8)} initial='hidden' animate='show' exit='hidden' className='hidden md:flex md:max-w-xl xl:max-w-none mx-auto xl:mx-0 mb-8'>
              <div className='flex flex-1 gap-x-6 xl:gap-x-12'>
                <div className='text-center'>
                  <div className='text-2xl xl:text-4xl font-extrabold text-accent mb-2'>
                    <CountUp start={0} end={yearsOfExperience} duration={5} /> +
                  </div>
                  <div className='text-xs uppercase tracking-[1px] leading-[1.4]'>Years of experience</div>
                </div>
                <div className='text-center'>
                  <div className='text-2xl xl:text-4xl font-extrabold text-accent mb-2'>
                    <CountUp start={0} end={finishedProjects} duration={5} /> +
                  </div>
                  <div className='text-xs uppercase tracking-[1px] leading-[1.4]'>Finished projects</div>
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
                          return <div key={itemIndex} className='text-2xl text-white'>{icon}</div>
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
