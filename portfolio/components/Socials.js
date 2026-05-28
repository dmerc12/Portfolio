import { RiInstagramLine, RiFacebookLine, RiLinkedinBoxLine, RiGithubLine } from 'react-icons/ri';
import Link from 'next/link';

const Socials = () => {
  return (
    <div className='flex items-center gap-x-5 text-lg'>
      <Link href={'https://www.facebook.com/dylan.mercer.3956'} className='hover:text-accent transition-all duration-300'><RiFacebookLine /></Link>
      <Link href={'https://www.instagram.com/dylanmercer12/'} className='hover:text-accent transition-all duration-300'><RiInstagramLine /></Link>
      <Link href={'https://www.linkedin.com/in/dylan-mercer-323666200/'} className='hover:text-accent transition-all duration-300'><RiLinkedinBoxLine /></Link>
      <Link href={'https://github.com/dmerc12'} className='hover:text-accent transition-all duration-300'><RiGithubLine /></Link>
    </div>
  );
};

export default Socials;
