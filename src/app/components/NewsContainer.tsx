"use client";

import { useEffect, useRef, useState } from "react";
import NewsCard from "./NewsCard";
import styles from "./NewsContainer.module.css";

interface NewsItem {
  summary: string;
  headline: string;
  source: string;
  url: string;
  image: string;
  category: string;
}

const NewsContainer: React.FC = () => {
  const containerRef = useRef<HTMLDivElement>(null);
  const [currentPage, setCurrentPage] = useState<number>(0);
  const [newsData, setNewsData] = useState<NewsItem[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string>("");

  useEffect(() => {
    async function fetchNews() {
      try {
        const response = await fetch("http://127.0.0.1:8000/news-summary");

        const data: NewsItem[] = await response.json();
        setNewsData(data);
      } catch (err) {
        console.error("Error fetching news data:", err);
        setError("Failed to fetch data");
      } finally {
        setLoading(false);
      }
    }
    fetchNews();
  }, []);

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

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  const numPages = Math.ceil(newsData.length / 2);

  return (
    <div className={styles.container} ref={containerRef}>
      {Array.from({ length: numPages }, (_, pageIndex) => (
        <div
          key={pageIndex}
          className={`${styles.newsPage} ${
            pageIndex === numPages - 1 ? styles.lastPage : ""
          }`}
        >
          {/* <NewsCard {...newsData[pageIndex]} /> */}
          {pageIndex === numPages - 1 ? (
            <NewsCard {...newsData[pageIndex * 2]} />
          ) : (
            <>
              <NewsCard {...newsData[pageIndex * 2]} />
              {newsData[pageIndex * 2 + 1] && (
                <NewsCard {...newsData[pageIndex * 2 + 1]} />
              )}
            </>
          )}
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
