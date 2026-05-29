import { HiHome, HiUser, HiViewColumns, HiEnvelope } from 'react-icons/hi2';
import { HiMenu, HiX } from 'react-icons/hi';
import { useRouter } from 'next/router';
import { useState } from 'react';
import Link from 'next/link';

export const navData = [
  { name: 'home', path: '/', icon: <HiHome /> },
  { name: 'about', path: '/about', icon: <HiUser /> },
  { name: 'work', path: '/work', icon: <HiViewColumns /> },
  { name: 'contact', path: '/contact', icon: <HiEnvelope /> },
];

const Nav = () => {
  const router = useRouter();
  const pathname = router.pathname;
  const [isOpen, setIsOpen] = useState(false);

  const toggleNav = () => setIsOpen(!isOpen);

  return (
      <>
        {/* Desktop navigation (always visible) */}
        <nav className='hidden xl:flex flex-col items-center justify-center gap-y-4 fixed right-[2%] z-50 top-0 h-screen w-16 max-w-md'>
          <div className='flex w-full xl:flex-col items-center justify-between xl:justify-center gap-y-10 px-4 md:px-40 xl:px-0 h-[80px] xl:h-max py-8 bg-white/10 backdrop-blur-sm text-3xl xl:text-xl xl:rounded-full'>
            {navData.map((link, index) => (
                <Link
                    key={index}
                    href={link.path}
                    className={`${link.path === pathname ? 'text-accent' : ''} relative flex items-center group hover:text-accent transition-all duration-300`}
                >
                  <div className='absolute pr-14 right-0 hidden group-hover:flex'>
                    <div className='bg-white relative flex text-primary items-center p-[6px] rounded-[3px]'>
                      <div className='text-[12px] leading-none font-semibold capitalize'>{link.name}</div>
                      <div className='border-solid border-l-white border-l-8 border-y-transparent border-y-[6px] border-r-0 absolute -right-2'></div>
                    </div>
                  </div>
                  <div>{link.icon}</div>
                </Link>
            ))}
          </div>
        </nav>

        {/* Mobile floating button */}
        <button
            onClick={toggleNav}
            className={`xl:hidden fixed right-4 z-50 bg-accent text-white p-3 rounded-full shadow-lg focus:outline-none ${isOpen ? 'bottom-16' : 'bottom-4'}`}
        >
          {isOpen ? <HiX size={24} /> : <HiMenu size={24} />}
        </button>

        {/* Mobile bottom navigation (conditionally visible) */}
        <nav
            className={`xl:hidden fixed bottom-0 left-0 w-full z-40 transition-transform duration-300 ease-in-out ${
                isOpen ? 'translate-y-0' : 'translate-y-full'
            }`}
        >
          <div className='flex items-center justify-around bg-white/10 backdrop-blur-sm py-4 text-2xl border-t border-white/20'>
            {navData.map((link, index) => (
                <Link
                    key={index}
                    href={link.path}
                    onClick={() => setIsOpen(false)} // close after navigation
                    className={`${link.path === pathname ? 'text-accent' : 'text-white'} hover:text-accent transition-colors duration-200`}
                >
                  {link.icon}
                </Link>
            ))}
          </div>
        </nav>
      </>
  );
};

export default Nav;
