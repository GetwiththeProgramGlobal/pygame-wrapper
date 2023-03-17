use std::process::Command;

fn main() {
    Command::new("python3").arg("main.py").spawn().expect("Failed to run game");
}
