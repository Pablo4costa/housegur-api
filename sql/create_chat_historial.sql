-- Create chat_historial table for storing conversation history
CREATE TABLE IF NOT EXISTS housegur.chat_historial (
  id INT PRIMARY KEY AUTO_INCREMENT,
  usuario_id INT NOT NULL,
  tipo_mensaje VARCHAR(10) NOT NULL,
  contenido TEXT NOT NULL,
  respuesta_asistente TEXT,
  accion_realizada VARCHAR(100),
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
  INDEX idx_usuario_timestamp (usuario_id, timestamp DESC)
);
