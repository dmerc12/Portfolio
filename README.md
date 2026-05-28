# Portfolio - Dylan Mercer

[![Deploy to AWS S3 and invalidate CloudFront](https://github.com/dmerc12/Portfolio/actions/workflows/deploy.yml/badge.svg)](https://github.com/dmerc12/Portfolio/actions/workflows/deploy.yml)

My personal software engineering portfolio – a responsive, static site built with Next.js, Tailwind CSS, and Framer Motion.
It showcases my projects, skills, work experience, and certifications, and includes a working contact form powered by Formspree.

👉 **[View the live site](https://dylanmercer.dev)**
👉 **[Current CloudFront URL](https://d3q34jrf9c485g.cloudfront.net/)**

---

## 🛠️ Technologies Used

- **Next.js** - React framework for static site generation (`output: 'export'`)
- **Tailwind CSS** - Utility-first styling
- **Framer Motion** - Page transitions and animations
- **Swiper** - Touch-friendly project carousel
- **React Toastify** - Form submission notifications
- **React Icons** - Skill icons and UI elements
- **Formspree** - Backend-less contact form (emails submissions to me)

### Deployment & Infrastructure

- **AWS S3** - Hosts the static files
- **AWS CloudFront** - CDN with HTTPS and Origin Access Control (OAC)
- **GitHub Actions** - CI/CD pipeline that runs `npm run build` and syncs the `out/` folder to S3, then invalidates CloudFront cache
- **Route 53** - Custom domain `dylanmercer.dev`

---

## 🚀 Getting Started (Local Development)

1. **Clone the repository**
    ```bash
    git clone https://github.com/dmerc12/Portfolio.git
    cd Portfolio/portfolio
    ```

2. **Install dependencies**
    ```bash
    npm ci
    ```

3. **Run the development server**
    ```bash
    npm run dev
    ```

4. **Open in browser**
    Open [http://localhost:3000](http://localhost:3000) to see the site.

5. **Build the static site locally**
    ```bash
    npm run build
    ```
    The static files will be  generated in the `out` directory.

---

## ☁️ CI/CD Deployment

Every push to the `main` branch triggers a GitHub Actions workflow that:
1. Installs Node.js dependencies
2. Runs `npm run build` (generates `portfolio/out/`)
3. Syncs the `out/` folder to the S3 bucket (`dylanmercer`)
4. Creates a CloudFront invalidation (`/*`) to clear the cache

### Required GitHub Secrets

| Secret Name | Description |
|-------------|-------------|
| `AWS_ACCESS_KEY_ID` | IAM user access key (with S3 write + CloudFront invalidation permissions) |
| `AWS_SECRET_ACCESS_KEY` | Corresponding secret key |
| `AWS_REGION` | us-east-2 |
| `AWS_S3_BUCKET` | dylanmercer |
| `AWS_CLOUDFRONT_DISTRIBUTION_ID` | Distribution ID for the CloudFront CDN |

---

## 📁 Project Structure

    ```txt
    portfolio/
    ├── components/       # Reusable React components (Avatar, Circles, WorkSlider, etc.)
    ├── pages/            # Next.js pages (index, about, contact, work)
    ├── public/           # Static assets (images, etc.)
    ├── styles/           # Global CSS (Tailwind imports)
    ├── next.config.js    # Next.js config (output: 'export', images.unoptimized)
    ├── tailwind.config.js
    └── package.json
    ```

---

## 📬 Contact

Feel free to reach out via the contact form or open an issue on this repository.

---

**Built by [Dylan Mercer](https://github.com/dmerc12)** - from full-stack to fourth grade and back.
