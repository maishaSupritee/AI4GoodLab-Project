import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "StreetScope.ai",
  description: "For data-driven cities",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased bg-[#EFF6FF]">{children}</body>
    </html>
  );
}