import styles from "./Header.module.css";

const Header = () => {
  return (
    <header className={styles.header} style={{ backgroundColor: "#1F3A93" }}>
      <h1 className={styles.title}>TOP THINGS OF THE DAY</h1>
    </header>
  );
};

export default Header;
