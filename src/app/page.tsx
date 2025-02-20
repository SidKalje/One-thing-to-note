import Header from "./components/Header";
import NewsContainer from "./components/NewsContainer";
import styles from "./page.module.css";
import LoadingAnimation from "./components/LoadingAnimation";
import { useState } from "react";

export default function Home() {
  const [loading, setLoading] = useState(true);

  return (
    <main className={styles.main}>
      <Header />
      <NewsContainer setLoading={setLoading} />
      {loading && <LoadingAnimation />}
    </main>
  );
}
