// "use client";

// import { motion } from "framer-motion";

// export default function LoadingAnimation() {
//   return (
//     <div className="fixed inset-0 flex items-center justify-center bg-opacity-0">
//       <div className="flex space-x-2">
//         {[0, 1, 2].map((index) => (
//           <motion.div
//             key={index}
//             className="w-4 h-4 bg-blue-500 rounded-full border-2 border-red-500"
//             animate={{ y: ["0%", "-100%", "0%"] }}
//             transition={{
//               duration: 0.8,
//               repeat: Infinity,
//               ease: "easeInOut",
//               delay: index * 0.15,
//             }}
//           />
//         ))}
//       </div>
//     </div>
//   );
// }
"use client";

import { motion } from "framer-motion";

export default function LoadingAnimation() {
  return (
    <div
      style={{
        position: "fixed",
        inset: 0,
        zIndex: 9999,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        // backgroundColor: "rgba(24, 24, 27, 0.8)", // Semi-transparent background
      }}
    >
      <div style={{ display: "flex", gap: "0.5rem" }}>
        {[0, 1, 2].map((index) => (
          <motion.div
            key={index}
            style={{
              width: "16px",
              height: "16px",
              backgroundColor: "#2b50ca", // blue-500
              borderRadius: "50%",
            }}
            animate={{ y: ["0%", "-100%", "0%"] }}
            transition={{
              duration: 0.8,
              repeat: Infinity,
              ease: "easeInOut",
              delay: index * 0.15,
            }}
          />
        ))}
      </div>
    </div>
  );
}
