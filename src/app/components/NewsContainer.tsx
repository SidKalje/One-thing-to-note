"use client";

import { useEffect, useRef, useState } from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import { Pagination, Navigation } from "swiper/modules";
import { mockNewsData } from "./mockData";
import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";
import NewsCard from "./NewsCard";
import styles from "./NewsContainer.module.css";
import LoadingAnimation from "./LoadingAnimation";
interface NewsItem {
  summary: string;
  headline: string;
  source: string;
  url: string;
  image: string;
  category: string;
}

interface NewsContainerProps {
  setLoading: (loading: boolean) => void;
}

const NewsContainer: React.FC<NewsContainerProps> = ({ setLoading }) => {
  const containerRef = useRef<HTMLDivElement>(null);
  const mockData = true;
  const [currentPage, setCurrentPage] = useState<number>(0);
  const [newsData, setNewsData] = useState<NewsItem[]>([]);
  const [error, setError] = useState<string>("");
  const hasFetched = useRef(false);
  useEffect(() => {
    if (mockData === true) {
      setNewsData(mockNewsData);
      setLoading(false);
      return;
    }
    async function fetchNews() {
      if (hasFetched.current) return;
      hasFetched.current = true;
      try {
        const response = await fetch("http://127.0.0.1:8000/news-summary");

        const data: NewsItem[] = await response.json();
        setNewsData(data);
      } catch (err) {
        console.error("Error fetching news data:", err);
        setError("Failed to fetch data");
      } finally {
        console.log("Setting loading to false");
        setLoading(false);
      }
    }

    fetchNews();
  }, [setLoading]);

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;

    const handleScroll = () => {
      const page = Math.round(container.scrollTop / container.clientHeight);
      setCurrentPage(page);
    };

    container.addEventListener("scroll", handleScroll);
    return () => container.removeEventListener("scroll", handleScroll);
  }, []);

  if (error) {
    return (
      <div>
        <LoadingAnimation />
      </div>
    );
  }

  // const numPages = Math.ceil(newsData.length / 2);
  const numPages = newsData.length;

  return (
    <div className={styles.container} ref={containerRef}>
      <Swiper
        modules={[Pagination, Navigation]}
        slidesPerView={1}
        loop={true}
        pagination={{ clickable: true }}
        navigation
        style={{ height: "100%" }}
      >
        {newsData.map((article, index) => (
          <SwiperSlide key={index}>
            <NewsCard {...article} />
          </SwiperSlide>
        ))}
      </Swiper>
    </div>
  );
};

export default NewsContainer;
