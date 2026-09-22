import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Luz de Luna Centro Ecuestre",
  description:
    "Equinoterapia, salto, adiestramiento y vaulting en Club Hipico - La Molina, Lima.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="es">
      <body className="bg-luna-fondo text-luna-texto">{children}</body>
    </html>
  );
}
