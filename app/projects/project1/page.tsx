import Link from 'next/link'
import { PROJECTS } from '@/app/data'
import { Magnetic } from '@/components/ui/magnetic'

export default function ProjectDemo() {
  const project = PROJECTS.find((p) => p.id === 'project1')

  if (!project) {
    return <div>Project not found</div>
  }

  return (
    <div className="mx-auto max-w-4xl px-4 py-20">
      <Magnetic springOptions={{ bounce: 0 }} intensity={0.3}>
        <Link
          href="/"
          aria-label="Back to home"
          className="mb-8 inline-block text-zinc-600 transition-colors hover:text-zinc-900 dark:text-zinc-400 dark:hover:text-zinc-100"
        >
          ←
        </Link>
      </Magnetic>

      <h1 className="mb-4 text-3xl font-medium">{project.name}</h1>
      <p className="mb-8 text-zinc-600 dark:text-zinc-400">
        {project.description}
      </p>

      <div className="space-y-8">
        <div className="rounded-2xl bg-zinc-50 p-1 ring-1 ring-zinc-200/50 dark:bg-zinc-950 dark:ring-zinc-800/50">
          {project.image ? (
            <img
              src={project.image}
              alt={project.name}
              className="aspect-video w-full rounded-xl object-cover bg-zinc-100 dark:bg-zinc-900"
            />
          ) : project.video ? (
            <video
              src={project.video}
              autoPlay
              loop
              muted
              playsInline
              className="aspect-video w-full rounded-xl bg-zinc-100 dark:bg-zinc-900"
            />
          ) : null}
        </div>

        <div className="prose prose-gray dark:prose-invert">
          <h2>Project Details</h2>
          <p>Placeholder project details content. Replace this with information about your project.</p>

          <h3>Features</h3>
          <ul>
            <li>Placeholder feature 1</li>
            <li>Placeholder feature 2</li>
            <li>Placeholder feature 3</li>
          </ul>

          <h3>Technologies</h3>
          <p>Placeholder technologies used in this project.</p>
        </div>
      </div>
    </div>
  )
}
