import Image from "next/image"
import styles from "./NewsCard.module.css"

interface NewsCardProps {
  headline: string
  summary: string
  thumbnail?: string
  category: string
}

const NewsCard = ({ headline, summary, thumbnail, category }: NewsCardProps) => {
  return (
    <article className={styles.card}>
      <div className={styles.category} style={{ backgroundColor: "#1F3A93" }}>
        {category}
      </div>
      {thumbnail && (
        <div className={styles.thumbnailContainer}>
          <Image src={thumbnail || "/placeholder.svg"} alt={headline} layout="fill" objectFit="cover" />
        </div>
      )}
      <div className={styles.content}>
        <h2 className={styles.headline}>{headline}</h2>
        <p className={styles.summary}>{summary}</p>
      </div>
    </article>
  )
}

export default NewsCard

