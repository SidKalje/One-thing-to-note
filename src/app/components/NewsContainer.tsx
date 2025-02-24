"use client";

import { useEffect, useRef, useState } from "react";
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
  const [currentPage, setCurrentPage] = useState<number>(0);
  const [newsData, setNewsData] = useState<NewsItem[]>([]);
  const [error, setError] = useState<string>("");

  const hasFetched = useRef(false);
  useEffect(() => {
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

  const numPages = Math.ceil(newsData.length / 2);

  return (
    <div className={styles.container} ref={containerRef}>
      {Array.from({ length: numPages }, (_, pageIndex) => (
        <div key={pageIndex} className={styles.newsPage}>
          {
            <>
              <NewsCard {...newsData[pageIndex * 2]} />
              {newsData[pageIndex * 2 + 1] && (
                <NewsCard {...newsData[pageIndex * 2 + 1]} />
              )}
            </>
          }
        </div>
      ))}
      <div className={styles.pageIndicator}>
        {Array.from({ length: numPages }, (_, index) => (
          <div
            key={index}
            className={`${styles.dot} ${
              index === currentPage ? styles.active : ""
            }`}
          />
        ))}
      </div>
    </div>
  );
};

export default NewsContainer;
