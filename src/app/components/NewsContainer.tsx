"use client";

import { useEffect, useRef, useState } from "react";
import NewsCard from "./NewsCard";
import styles from "./NewsContainer.module.css";

const [techData, setTechData] = useState(null);

const mockNews = [
  {
    id: 1,
    headline: "",
    summary:
      "Scientists announce a revolutionary advancement in quantum computing, promising to reshape the future of technology.",
    thumbnail: "/placeholder.svg?height=200&width=300",
    category: "Tech",
  },
  {
    id: 2,
    headline: "Global Climate Summit Concludes",
    summary: "World, leaders",
    thumbnail: "/placeholder.svg?height=200&width=300",
    category: "Politics",
  },
  {
    id: 3,
    headline: "New Art Installation Captivates City",
    summary:
      "A stunning interactive sculpture transforms the city's skyline, drawing crowds and sparking conversations.",
    thumbnail: "/placeholder.svg?height=200&width=300",
    category: "Entertainment",
  },
  {
    id: 4,
    headline: "Sports: Underdog Team Wins Championship",
    summary:
      "In a thrilling upset, the underdog team clinches the championship title, ending a 50-year drought.",
    thumbnail: "/placeholder.svg?height=200&width=300",
    category: "Sports",
  },
  {
    id: 5,
    headline: "Health: Breakthrough in Cancer Research",
    summary:
      "Researchers discover a promising new treatment that shows remarkable results in early-stage clinical trials.",
    thumbnail: "/placeholder.svg?height=200&width=300",
    category: "Health",
  },
];

const NewsContainer = () => {
  const containerRef = useRef<HTMLDivElement>(null);
  const [currentPage, setCurrentPage] = useState(0);

  useEffect(() => {
    async function fetchNews() {
      const response = await fetch("https://api.example.com/news");
      const data = await response.json();
      setTechData(data);
    }
  });
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

  return (
    <div className={styles.container} ref={containerRef}>
      {Array.from(
        { length: Math.ceil(mockNews.length / 2) },
        (_, pageIndex) => (
          <div
            key={pageIndex}
            className={`${styles.newsPage} ${
              pageIndex === Math.floor(mockNews.length / 2)
                ? styles.lastPage
                : ""
            }`}
          >
            {pageIndex === Math.floor(mockNews.length / 2) ? (
              <NewsCard {...mockNews[pageIndex * 2]} />
            ) : (
              <>
                <NewsCard {...mockNews[pageIndex * 2]} />
                {mockNews[pageIndex * 2 + 1] && (
                  <NewsCard {...mockNews[pageIndex * 2 + 1]} />
                )}
              </>
            )}
          </div>
        )
      )}
      <div className={styles.pageIndicator}>
        {Array.from({ length: Math.ceil(mockNews.length / 2) }, (_, index) => (
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
