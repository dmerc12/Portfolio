import { Swiper, SwiperSlide } from 'swiper/react';
import { BsArrowRight } from 'react-icons/bs';
import { Pagination } from 'swiper/modules';
import Image from 'next/image';
import 'swiper/css/pagination';
import Link from 'next/link';
import 'swiper/css';

const workSlides = {
  slides: [
    {
      images: [
        {
          title: 'Oklahoma Handyman',
          path: '/oklahoma-handyman.png',
          url: 'https://github.com/theoklahomahandyman/the-oklahoma-handyman-service-website',
        },
        {
          title: 'Bear Points',
          path: '/bearpoints.png',
          url: 'https://github.com/dmerc12/BearPoints'
        },
        {
          title: 'About OK',
          path: '/about-ok.png',
          url: 'https://github.com/dmerc12/About-OK'
        },
        {
          title: 'Portfolio (This website)',
          path: '/portfolio.png',
          url: 'https://github.com/dmerc12/Portfolio'
        },
      ],
    },
  ],
};

const WorkSlider = () => {
  return (
    <Swiper spaceBetween={5} pagination={{ clickable: true }} modules={[Pagination]} className='h-[640px] sm:h-[720px]'>
      {workSlides.slides.map((slide, index) => {
        return (
          <SwiperSlide key={index}>
            <div className='grid grid-cols-2 grid-rows-2 gap-4 cursor-pointer'>
              {slide.images.map((image, index) => {
                return (
                  <div className='relative rounded-lg overflow-hidden flex items-center justify-center group' key={index}>
                    <div className='flex items-center justify-center relative overflow-hidden group'>
                      <Image src={image.path} width={500} height={300} alt='' />
                      <div className='absolute inset-0 bg-gradient-to-l from-transparent via-[#e838cc] to-[#4a22bd] opacity-0 group-hover:opacity-80 transition-all duration-700'></div>
                      <div className='absolute bottom-0 translate-y-full group-hover:-translate-y-10 group-hover:xl:-translate-y-20 transition-all duration-300'>
                        <p className='text-center'>{image.title}</p>
                        {/* <div className='flex items-center gap-x-2 text-[13px] tracking-[0.2em]'>
                          <div className='delay-100'>LIVE</div>
                          <div className='translate-y-[500%] group-hover:translate-y-0 transition-all duration-300 delay-150'>PROJECT</div>
                          <div className='text-xl translate-y-[500%] group-hover:translate-y-0 transition-all duration-300 delay-200'><BsArrowRight /></div>
                        </div> */}
                        <Link href={image.url}>
                          <div className='flex items-center gap-x-2 text-[13px] tracking-[0.2em]'>
                            <div className='delay-100'>PROJECT</div>
                            <div className='translate-y-[500%] group-hover:translate-y-0 transition-all duration-300 delay-150'>DETAILS</div>
                            <div className='text-xl translate-y-[500%] group-hover:translate-y-0 transition-all duration-300 delay-200'><BsArrowRight /></div>
                          </div>
                        </Link>
                      </div>
                    </div>
                  </div>
                )
              })}
            </div>
          </SwiperSlide>
        );
      })}
    </Swiper>
  );
};

export default WorkSlider;
