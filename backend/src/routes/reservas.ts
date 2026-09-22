import { Router } from "express";
import { z } from "zod";

const router = Router();

// Placeholder en memoria - se reemplaza por Prisma/Postgres en el siguiente paso.
const reservas: Array<{ id: string; claseId: string; nombreCliente: string }> = [];

const crearReservaSchema = z.object({
  claseId: z.string().min(1),
  nombreCliente: z.string().min(2),
});

router.get("/", (_req, res) => {
  res.json(reservas);
});

router.post("/", (req, res) => {
  const parsed = crearReservaSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.flatten() });
  }

  const nueva = {
    id: String(reservas.length + 1),
    ...parsed.data,
  };
  reservas.push(nueva);
  res.status(201).json(nueva);
});

export default router;
