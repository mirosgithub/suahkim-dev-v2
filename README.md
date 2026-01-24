# suahkim-dev-v2

![Website Deploy](https://deploy-badge.vercel.app/?url=http%3A%2F%2Fsuahkim.dev&style=flat-square&logo=Vercel&name=Vercel)

Personal portfolio website built with [Next.js](https://nextjs.org/), deployed to [Vercel](https://vercel.com).

## Migration

This project was recently migrated from [Reflex](https://reflex.dev/) (Python-based web framework) deployed on Google Cloud Run to Next.js on Vercel. The migration was driven by:

- **Deployment costs**: Vercel's free tier provides a more cost-effective solution for a personal portfolio compared to Cloud Run's per-request pricing model
- **Frontend functionality**: Next.js offers more extensive frontend capabilities and a richer ecosystem for building modern web experiences

## Deployment

Deploys automatically on pushes to `main` via Vercel. The deployment status badge above shows the current deployment status.

## Local development

### Prerequisites

- Node.js 20.x or later
- npm or yarn

### Setup

```bash
# Install dependencies
npm install

# Run development server
npm run dev
```

The app will be available at [http://localhost:3000](http://localhost:3000).

### Available scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint

## Tech stack

- [Next.js 15](https://nextjs.org/) - React framework
- [TypeScript](https://www.typescriptlang.org/) - Type safety
- [Tailwind CSS](https://tailwindcss.com/) - Styling
- [MDX](https://mdxjs.com/) - Blog posts
- [Motion](https://motion-primitives.com/) - Animations
