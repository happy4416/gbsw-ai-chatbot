'use client';

import { useState, useEffect } from 'react';
import axios from 'axios';

const API_URL = 'http://localhost:8000';

interface Message {
  role: 'user' | 'assistant';
  content: string;
  sources?: string[];
}

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [models, setModels] = useState<string[]>([]);
  const [selectedModel, setSelectedModel] = useState('neural-chat:latest');
  const [health, setHealth] = useState<any>({});

  useEffect(() => {
    checkHealth();
    fetchModels();
  }, []);

  const checkHealth = async () => {
    try {
      const response = await axios.get(`${API_URL}/api/health`);
      setHealth(response.data);
    } catch {
      setHealth({ status: 'error' });
    }
  };

  const fetchModels = async () => {
    try {
      const response = await axios.get(`${API_URL}/api/models`);
      const modelNames = response.data.models?.map((m: any) => m.name) || [];
      setModels(modelNames);
      if (modelNames.length > 0) {
        setSelectedModel(modelNames[0]);
      }
    } catch (error) {
      console.error('Failed to fetch models:', error);
    }
  };

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage: Message = { role: 'user', content: input };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await axios.post(`${API_URL}/api/chat`, {
        message: input,
        model: selectedModel
      });

      const assistantMessage: Message = {
        role: 'assistant',
        content: response.data.response,
        sources: response.data.sources
      };
      setMessages(prev => [...prev, assistantMessage]);
    } catch (error: any) {
      const errorMessage: Message = {
        role: 'assistant',
        content: `오류: ${error.response?.data?.detail || '응답을 가져올 수 없습니다'}`
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '900px', margin: '0 auto', padding: '20px' }}>
      <h1 style={{ textAlign: 'center', color: '#2c3e50' }}>🎓 경북소프트웨어마이스터고 도우미 AI</h1>
      
      <div style={{ marginBottom: '20px', padding: '15px', background: '#ecf0f1', borderRadius: '10px' }}>
        <div style={{ marginBottom: '10px' }}>
          <strong>상태:</strong> {health.status || 'checking...'}
          {' | '}
          <strong>Ollama:</strong> {health.ollama || 'checking...'}
          {' | '}
          <strong>문서:</strong> {health.documents || 0}개
        </div>
        <label>
          <strong>모델:</strong>{' '}
          <select 
            value={selectedModel} 
            onChange={(e) => setSelectedModel(e.target.value)}
            style={{ padding: '5px', borderRadius: '5px', border: '1px solid #bdc3c7' }}
          >
            {models.map(model => (
              <option key={model} value={model}>{model}</option>
            ))}
          </select>
        </label>
      </div>

      <div style={{ 
        border: '2px solid #3498db', 
        borderRadius: '10px', 
        padding: '20px', 
        minHeight: '450px',
        maxHeight: '550px',
        overflowY: 'auto',
        marginBottom: '20px',
        background: 'white'
      }}>
        {messages.length === 0 && (
          <div style={{ textAlign: 'center', color: '#7f8c8d', marginTop: '50px' }}>
            <h2>경북소프트웨어마이스터고에 대해 물어보세요!</h2>
            <div style={{ marginTop: '30px', fontSize: '14px' }}>
              <p>💡 예시 질문:</p>
              <p>• 학교 위치가 어디인가요?</p>
              <p>• 어떤 학과가 있나요?</p>
              <p>• 입학 방법을 알려주세요</p>
              <p>• 병역특례가 가능한가요?</p>
            </div>
          </div>
        )}
        {messages.map((msg, idx) => (
          <div 
            key={idx} 
            style={{ 
              marginBottom: '20px',
              padding: '15px',
              borderRadius: '10px',
              background: msg.role === 'user' ? '#3498db' : '#ecf0f1',
              color: msg.role === 'user' ? 'white' : 'black',
              marginLeft: msg.role === 'user' ? '80px' : '0',
              marginRight: msg.role === 'user' ? '0' : '80px'
            }}
          >
            <strong>{msg.role === 'user' ? '👤 나' : '🤖 AI'}:</strong>
            <p style={{ margin: '10px 0 0 0', whiteSpace: 'pre-wrap', lineHeight: '1.6' }}>{msg.content}</p>
            {msg.sources && msg.sources.length > 0 && (
              <div style={{ marginTop: '10px', paddingTop: '10px', borderTop: '1px solid #bdc3c7', fontSize: '12px', opacity: 0.8 }}>
                📚 출처: {msg.sources.join(', ')}
              </div>
            )}
          </div>
        ))}
        {loading && (
          <div style={{ textAlign: 'center', color: '#7f8c8d' }}>
            <p>💭 생각하는 중...</p>
          </div>
        )}
      </div>

      <div style={{ display: 'flex', gap: '10px' }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && !loading && sendMessage()}
          placeholder="질문을 입력하세요..."
          disabled={loading}
          style={{ 
            flex: 1, 
            padding: '15px', 
            fontSize: '16px',
            borderRadius: '10px',
            border: '2px solid #3498db'
          }}
        />
        <button
          onClick={sendMessage}
          disabled={loading || !input.trim()}
          style={{ 
            padding: '15px 30px', 
            fontSize: '16px',
            borderRadius: '10px',
            border: 'none',
            background: loading || !input.trim() ? '#bdc3c7' : '#3498db',
            color: 'white',
            cursor: loading || !input.trim() ? 'not-allowed' : 'pointer',
            fontWeight: 'bold'
          }}
        >
          전송
        </button>
      </div>
    </div>
  );
}
