import Header from "./components/Header"
import NewsContainer from "./components/NewsContainer"
import styles from "./page.module.css"

export default function Home() {
  return (
    <main className={styles.main}>
      <Header />
      <NewsContainer />
    </main>
  )
}

