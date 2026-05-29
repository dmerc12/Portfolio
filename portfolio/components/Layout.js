import TopLeftImg from '../components/TopLeftImg';
import Header from '../components/Header';
import { Sora } from '@next/font/google';
import Nav from '../components/Nav';

const sora = Sora({
  subsets: ['latin'],
  variable: '--font-sora',
  weight: ['100', '200', '300', '400', '500', '600', '700', '800']
})

const Layout = ({ children }) => {
  return (
    <div className={`page bg-site text-white bg-cover bg-no-repeat ${sora.variable} font-sora relative`}>
      <TopLeftImg />
      <Nav />
      <Header />
      <main className='relative h-full mb-3 mt-3 pb-2 pt-2'>
          { children }
      </main>
    </div>
  );
};

export default Layout;
