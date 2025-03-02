import Image from "next/image";
import styles from "./NewsCard.module.css";

interface NewsCardProps {
  summary: string; // Expected to be valid HTML
  headline: string;
  source: string;
  url: string;
  image: string;
  category: string;
}

const NewsCard = ({
  headline,
  summary,
  image: thumbnail,
  url,
  category,
}: NewsCardProps) => {
  return (
    <div className={styles.wrapper}>
      <div className={styles.categoryTab}>{category}</div>
      <article className={styles.card}>
        {thumbnail && (
          <div className={styles.thumbnailContainer}>
            <Image
              src={thumbnail || "/placeholder.svg"}
              alt={headline}
              layout="fill"
              objectFit="cover"
            />
          </div>
        )}
        <div className={styles.content}>
          <h2 className={styles.headline}>
            <a href={url} target="_blank" rel="noopener noreferrer">
              <u>{headline}</u>
            </a>
          </h2>
          <div
            className={styles.summary}
            dangerouslySetInnerHTML={{ __html: summary }}
          />
        </div>
      </article>
    </div>
  );
};

export default NewsCard;
