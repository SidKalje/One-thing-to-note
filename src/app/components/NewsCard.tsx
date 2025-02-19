import Image from "next/image";
import styles from "./NewsCard.module.css";

interface NewsCardProps {
  summary: string; // This is expected to be valid HTML
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
    <article className={styles.card}>
      <div className={styles.category} style={{ backgroundColor: "#1F3A93" }}>
        {category}
      </div>
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
            {headline}
          </a>
        </h2>
        <div
          className={styles.summary}
          dangerouslySetInnerHTML={{ __html: summary }}
        />
      </div>
    </article>
  );
};

export default NewsCard;
