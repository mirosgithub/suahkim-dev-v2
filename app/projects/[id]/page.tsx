import Link from 'next/link'
import { PROJECTS } from '@/app/data'
import { Magnetic } from '@/components/ui/magnetic'

export default async function ProjectPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const project = PROJECTS.find((p) => p.id === id)

  if (!project) {
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
        <div className="text-zinc-600 dark:text-zinc-400">Project not found.</div>
      </div>
    )
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

      <h1 className="mb-4 text-3xl font-medium text-zinc-900 dark:text-zinc-50">
        {project.name}
      </h1>
      <p className="mb-8 text-zinc-600 dark:text-zinc-400">{project.description}</p>

      <div className="space-y-8">
        {(project.image || project.video) && (
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
        )}

        <div className="prose prose-gray dark:prose-invert">
          <h2>Project details</h2>
          <p>
            Placeholder for project details.
          </p>
        </div>
      </div>
    </div>
  )
}

