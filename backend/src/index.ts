import express from "express";
import cors from "cors";
import helmet from "helmet";
import rateLimit from "express-rate-limit";
import dotenv from "dotenv";
import healthRouter from "./routes/health";
import reservasRouter from "./routes/reservas";

dotenv.config();

const app = express();
const PORT = process.env.PORT || 4000;

// --- Seguridad basica ---
app.use(helmet());
app.use(
  cors({
    origin: process.env.NEXT_PUBLIC_API_URL ? true : "*",
    credentials: true,
  })
);
app.use(express.json({ limit: "1mb" }));

// Limite de peticiones para evitar abuso (fuerza bruta, scraping, etc.)
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutos
  limit: 300,
  standardHeaders: true,
  legacyHeaders: false,
});
app.use(limiter);

// --- Rutas ---
app.use("/api/health", healthRouter);
app.use("/api/reservas", reservasRouter);

app.use((_req, res) => {
  res.status(404).json({ error: "Ruta no encontrada" });
});

app.listen(PORT, () => {
  console.log(`Backend Luz de Luna escuchando en el puerto ${PORT}`);
});
