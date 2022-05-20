const { promisify } = require('util'),
  exec = promisify(require('child_process').exec)

async function main() {
    const docker_check = await exec('docker --version')
    if (docker_check.stderr.length > 0) {
        console.log('\x1b[31m', 'Error:', '\x1b[0m', 'Docker is not installed. Please install Docker and try again.')
        process.exit(1)
    }
    if (process.platform === "win32" || process.platform === "win64") {
        const result = await exec(`.\\layer-generator\\build.bat`)
        console.log(result.stdout)
    } else {
        const result = await exec(`./layer-generator/build.sh`)
        console.log(result.stdout)
    }
}

main()