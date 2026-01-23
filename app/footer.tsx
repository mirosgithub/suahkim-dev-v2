'use client'
import { AnimatedBackground } from '@/components/ui/animated-background'
import { Magnetic } from '@/components/ui/magnetic'
import { TextLoop } from '@/components/ui/text-loop'
import { MonitorIcon, MoonIcon, SunIcon } from 'lucide-react'
import { useTheme } from 'next-themes'
import { useEffect, useState } from 'react'

const THEMES_OPTIONS = [
  {
    label: 'Light',
    id: 'light',
    icon: <SunIcon className="h-4 w-4" />,
  },
  {
    label: 'Dark',
    id: 'dark',
    icon: <MoonIcon className="h-4 w-4" />,
  },
  {
    label: 'System',
    id: 'system',
    icon: <MonitorIcon className="h-4 w-4" />,
  },
]

function ThemeSwitch() {
  const [mounted, setMounted] = useState(false)
  const { theme, setTheme } = useTheme()

  useEffect(() => {
    setMounted(true)
  }, [])

  if (!mounted) {
    return null
  }

  return (
    <div className="inline-flex">
      <AnimatedBackground
        className="pointer-events-none rounded-lg backdrop-blur-xl bg-white/40 dark:bg-gray-900/40 border border-white/50 dark:border-gray-700/50 shadow-2xl"
        defaultValue={theme}
        transition={{
          type: 'spring',
          bounce: 0,
          duration: 0.2,
        }}
        enableHover={true}
        onValueChange={(id) => {
          setTheme(id as string)
        }}
      >
        {THEMES_OPTIONS.map((theme) => {
          return (
            <Magnetic key={theme.id} springOptions={{ bounce: 0 }} intensity={0.3}>
              <button
                className="inline-flex h-7 w-7 items-center justify-center text-zinc-500 transition-colors duration-100 focus-visible:outline-2 data-[checked=true]:text-zinc-950 dark:text-zinc-100 dark:data-[checked=true]:text-zinc-50 hover:text-zinc-600 dark:hover:text-zinc-300"
                type="button"
                aria-label={`Switch to ${theme.label} theme`}
                data-id={theme.id}
              >
                {theme.icon}
              </button>
            </Magnetic>
          )
        })}
      </AnimatedBackground>
    </div>
  )
}

export function Footer() {
  return (
    <footer className="mt-24 border-t border-zinc-100 px-0 py-4 dark:border-zinc-800">
      <div className="flex items-center justify-between">
        <a href="https://github.com/mirosgithub" target="_blank">
          <TextLoop className="text-xs text-zinc-500">
            <span>© 2026 Suah Kim</span>
            <span>Built with Next.js</span>
          </TextLoop>
        </a>
        <div className="text-xs text-zinc-400">
          <ThemeSwitch />
        </div>
      </div>
    </footer>
  )
}
